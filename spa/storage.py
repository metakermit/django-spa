from django.contrib.staticfiles.storage import ManifestStaticFilesStorage
from whitenoise.storage import HelpfulExceptionMixin, CompressedStaticFilesMixin

class PatchedManifestStaticFilesStorage(ManifestStaticFilesStorage):
    """
    A static file system storage backend which also saves
    hashed copies of the files it saves.
    """

    def url_converter(self, *args, **kwargs):
        """
        Return the custom URL converter for the given file name.
        """
        upstream_converter = super(PatchedManifestStaticFilesStorage, self).url_converter(*args, **kwargs)

        def converter(matchobj):
            try:
                upstream_converter(matchobj)
            except ValueError:
                # e.g. a static file 'static/media/logo.6a30f15f.svg' could not be found
                # because the upstream converter stripped 'static/' from the path
                matched, url = matchobj.groups()
                return matched

        return converter

class SPAStaticFilesStorage(
        HelpfulExceptionMixin, CompressedStaticFilesMixin,
        PatchedManifestStaticFilesStorage):
    pass
