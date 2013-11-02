from github3.repos.release import Release, Asset

from .helper import UnitHelper


def releases_url(path=''):
    url = "https://api.github.com/repos/octocat/Hello-World/releases"
    return url + path


class TestRelease(UnitHelper):
    described_class = Release
    example_data = {
        "url": releases_url("/1"),
        "html_url": "https://github.com/octocat/Hello-World/releases/v1.0.0",
        "assets_url": releases_url("/1/assets"),
        "upload_url": releases_url("/1/assets{?name}"),
        "id": 1,
        "tag_name": "v1.0.0",
        "target_commitish": "master",
        "name": "v1.0.0",
        "body": "Description of the release",
        "draft": False,
        "prerelease": False,
        "created_at": "2013-02-27T19:35:32Z",
        "published_at": "2013-02-27T19:35:32Z"
        }

    def test_has_upload_urlt(self):
        assert self.instance.upload_urlt is not None


class TestAsset(UnitHelper):
    described_class = Asset
    example_data = {
        "url": releases_url("/assets/1"),
        "id": 1,
        "name": "example.zip",
        "label": "short description",
        "state": "uploaded",
        "content_type": "application/zip",
        "size": 1024,
        "download_count": 42,
        "created_at": "2013-02-27T19:35:32Z",
        "updated_at": "2013-02-27T19:35:32Z"
        }