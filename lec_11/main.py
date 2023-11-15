import requests

api_base_url = "https://jsonplaceholder.typicode.com/"

fetched_posts_response = requests.get(f"{api_base_url}/posts")

if fetched_posts_response.status_code == 200:
    fetched_posts_data = fetched_posts_response.json()

      # Filtering the titles
    short_titles_list = []
    for post_item in fetched_posts_data:
        if len(post_item['title'].split()) <= 6:
            short_titles_list.append(post_item['title'])

    print("Titles with 6 words or fewer:")

    for short_title_item in short_titles_list:
        print(short_title_item)

      # Filtering the posts
    brief_posts_list = []

    for post_item in fetched_posts_data:
        if len(post_item['body'].split('\n')) <= 3:
            brief_posts_list.append(post_item)

    print("\nPosts with body containing 3 or fewer lines:")
    for brief_post_item in brief_posts_list:
        print(f"\nTitle: {brief_post_item['title']}")
        print(f"Body:\n{brief_post_item['body']}")
else:
     print("Failed to fetch posts.")

my_new_post_data = {"title": "My New Title", "body": "Some new text"}
new_post_response = requests.post(f"{api_base_url}/posts", json=my_new_post_data)

if new_post_response.status_code == 201:
    my_new_post_id = new_post_response.json()['id']
    print(f"ID of my_new_post: {my_new_post_id}")

my_updated_post_data = {"title": "Updated Title", "body": "Some updated text"}
update_response = requests.put(f"{api_base_url}/posts/{my_new_post_id}", json=my_updated_post_data)

if update_response.status_code == 200:
    print("The post my_new_post updated successfully")

delete_response = requests.delete(f"{api_base_url}/posts/{my_new_post_id}")
if delete_response.status_code == 200:
    print("The post my_new_post deleted successfully")
