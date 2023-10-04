def __init__(hub):
    hub.exec.oci.ENDPOINT_URLS = ["/20160918"]
    # The default is the first in the list
    hub.exec.oci.DEFAULT_ENDPOINT_URL = "/20160918"

    # This enables acct profiles that begin with "oci" for oci modules
    hub.exec.oci.ACCT = ["oci"]
