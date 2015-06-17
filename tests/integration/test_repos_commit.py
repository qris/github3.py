"""Integration tests for Repository Commit objects."""
import github3

from . import helper


class TestRepoCommit(helper.IntegrationHelper):

    """Integration tests for the RepoCommit object."""

    def test_statuses(self):
        """Test the ability to retrieve statuses on a commit."""
        cassette_name = self.cassette_name('statuses')
        with self.recorder.use_cassette(cassette_name):
            repository = self.gh.repository('sigmavirus24', 'github3.py')
            commit = repository.commit(
                '29eaea046b353723f80a4810e3f2ea9d16ea6c25'
            )
            statuses = list(commit.statuses())

        for status in statuses:
            assert isinstance(status, github3.repos.status.Status)

    def test_comments(self):
        """Test the ability to retrieve comments on a commit."""
        cassette_name = self.cassette_name('comments')
        with self.recorder.use_cassette(cassette_name):
            repository = self.gh.repository('octocat', 'Hello-World')
            commit = repository.commit(
                '553c2077f0edc3d5dc5d17262f6aa498e69d6f8e'
            )
            comments = list(commit.comments())

        for comment in comments:
            assert isinstance(comment, github3.repos.comment.RepoComment)
