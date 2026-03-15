import allure
import pytest

from src.core.assertions import assert_has_keys, assert_status_code
from src.core.parsers import to_comment, to_post, to_user
from src.data.post_payloads import NEW_POST_PAYLOAD, UPDATED_POST_PAYLOAD


@allure.epic("JSONPlaceholder API")
@allure.feature("Posts")
@pytest.mark.e2e
def test_user_post_comments_flow(posts_client, users_client, comments_client):
    with allure.step("Get post by id"):
        post_response = posts_client.get_post(1)
        assert_status_code(post_response, 200)
        post_payload = post_response.json()
        assert_has_keys(post_payload, ("userId", "id", "title", "body"))
        post = to_post(post_payload)

    with allure.step("Get post author by user id"):
        user_response = users_client.get_user(post.userId)
        assert_status_code(user_response, 200)
        user_payload = user_response.json()
        assert_has_keys(
            user_payload,
            ("id", "name", "username", "email", "address", "phone", "website", "company"),
        )
        user = to_user(user_payload)

    with allure.step("Get comments linked to the post"):
        comments_response = comments_client.get_comments_by_post(post.id)
        assert_status_code(comments_response, 200)
        comments_payload = comments_response.json()
        assert comments_payload, "Expected comments for the selected post"
        comments = [to_comment(item) for item in comments_payload]

    assert user.id == post.userId, "Post author does not match linked user"
    assert user.address.city, "User city should not be empty"
    assert user.address.geo.lat, "User geo latitude should not be empty"
    assert user.company.name, "User company name should not be empty"
    assert all(comment.postId == post.id for comment in comments), "Found comment not linked to selected post"
    assert comments[0].email, "Comment email should not be empty"


@allure.epic("JSONPlaceholder API")
@allure.feature("Posts")
@pytest.mark.e2e
def test_create_post(posts_client):
    with allure.step("Create a new post"):
        response = posts_client.create_post(NEW_POST_PAYLOAD)
        assert_status_code(response, 201)
        payload = response.json()

    assert_has_keys(payload, ("title", "body", "userId", "id"))
    assert payload["title"] == NEW_POST_PAYLOAD["title"]
    assert payload["body"] == NEW_POST_PAYLOAD["body"]
    assert payload["userId"] == NEW_POST_PAYLOAD["userId"]
    assert payload["id"] > 0


@allure.epic("JSONPlaceholder API")
@allure.feature("Posts")
@pytest.mark.e2e
def test_update_and_delete_post(posts_client):
    with allure.step("Update post"):
        update_response = posts_client.update_post(1, UPDATED_POST_PAYLOAD)
        assert_status_code(update_response, 200)
        updated_payload = update_response.json()

    assert_has_keys(updated_payload, ("title", "body", "userId", "id"))
    assert updated_payload["id"] == UPDATED_POST_PAYLOAD["id"]
    assert updated_payload["title"] == UPDATED_POST_PAYLOAD["title"]
    assert updated_payload["body"] == UPDATED_POST_PAYLOAD["body"]

    with allure.step("Delete post"):
        delete_response = posts_client.delete_post(UPDATED_POST_PAYLOAD["id"])
        assert_status_code(delete_response, 200)
        assert delete_response.json() == {}, "Expected empty response body after delete"
