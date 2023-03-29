import unittest
import requests, json

class TestJava(unittest.TestCase):

    def test_signals(self):
        URL = "https://api.github.com/search/repositories?q=language:java&sort=stars"
        headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"}
        req = requests.get(URL, headers=headers)
        self.assertEqual(req.status_code, 200)

    def test_numbers_elements(self):
        URL = "https://api.github.com/search/repositories?q=language:java&sort=stars"
        headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"}
        req = requests.get(URL, headers=headers)
        data = req.json()
        all_data_keys = data['items'][0].keys()
        self.assertEqual(list(all_data_keys), ['id', 'node_id', 'name', 'full_name', 'private', 'owner', 'html_url', 'description', 'fork', 'url', 'forks_url', 'keys_url', 'collaborators_url', 'teams_url', 'hooks_url', 'issue_events_url', 'events_url', 'assignees_url', 'branches_url', 'tags_url', 'blobs_url', 'git_tags_url', 'git_refs_url', 'trees_url', 'statuses_url', 'languages_url', 'stargazers_url', 'contributors_url', 'subscribers_url', 'subscription_url', 'commits_url', 'git_commits_url', 'comments_url', 'issue_comment_url', 'contents_url', 'compare_url', 'merges_url', 'archive_url', 'downloads_url', 'issues_url', 'pulls_url', 'milestones_url', 'notifications_url', 'labels_url', 'releases_url', 'deployments_url', 'created_at', 'updated_at', 'pushed_at', 'git_url', 'ssh_url', 'clone_url', 'svn_url', 'homepage', 'size', 'stargazers_count', 'watchers_count', 'language', 'has_issues', 'has_projects', 'has_downloads', 'has_wiki', 'has_pages', 'has_discussions', 'forks_count', 'mirror_url', 'archived', 'disabled', 'open_issues_count', 'license', 'allow_forking', 'is_template', 'web_commit_signoff_required', 'topics', 'visibility', 'forks', 'open_issues', 'watchers', 'default_branch', 'score'])

    def count_repositories(self):
        URL = "https://api.github.com/search/repositories?q=language:java&sort=stars"
        headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"}
        req = requests.get(URL, headers=headers)
        data = req.json()
        self.assertNotEqual(data['total_count'], 0)
        self.assertNotEqual(data['total_count'], 1)
        self.assertNotEqual(data['total_count'], -1)

if __name__ == "__main__":
    TestJava.main()