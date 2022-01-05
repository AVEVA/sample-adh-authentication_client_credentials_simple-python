# OSIsoft Cloud Services Client Credentials Python Sample

**Version:** 1.0.0

[![Build Status](https://dev.azure.com/osieng/engineering/_apis/build/status/product-readiness/OCS/osisoft.sample-ocs-authentication_client_credentials_simple-python?repoName=osisoft%2Fsample-ocs-authentication_client_credentials_simple-python&branchName=main)](https://dev.azure.com/osieng/engineering/_build/latest?definitionId=4392&repoName=osisoft%2Fsample-ocs-authentication_client_credentials_simple-python&branchName=main)

Developed against Python 3.9.5.

## Requirements

- Python 3.9+
- Register a [Client-Credentials Client](https://cloud.osisoft.com/clients) in your OSIsoft Cloud Services tenant and create a client secret to use in the configuration of this sample. ([Video Walkthrough](https://www.youtube.com/watch?v=JPWy0ZX9niU))
- Install required modules: `pip install -r requirements.txt`

## About this sample

This sample is meant to be a very simple and straightforward to show how you can use common python library calls to authenticate against OCS.  In a more complete application you should reuse the bearer token as appropriate and only reissue a new token when it is about to timeout.  

Steps:
1. Get needed variables
1. Get the authentication endpoint from the discovery URL
1. Use the client ID and Secret to get the bearer token from the authentication endpoint
1. Test it by calling the base tenant endpoint and making sure a valid response is returned

## Configuring the sample

The sample is configured using the file [appsettings.placeholder.json](appsettings.placeholder.json). Before editing, rename this file to `appsettings.json`. This repository's `.gitignore` rules should prevent the file from ever being checked in to any fork or branch, to ensure credentials are not compromised.

OSIsoft Cloud Services is secured by obtaining tokens from its identity endpoint. Client credentials clients provide a client application identifier and an associated secret (or key) that are authenticated against the token endpoint. You must replace the placeholders in your `appsettings.json` file with the authentication-related values from your tenant and a client-credentials client created in your OCS tenant.

```json
{
  "Resource": "https://dat-b.osisoft.com",
  "ApiVersion": "v1",
  "TenantId": "PLACEHOLDER_REPLACE_WITH_TENANT_ID",
  "ClientId": "PLACEHOLDER_REPLACE_WITH_APPLICATION_IDENTIFIER",
  "ClientSecret": "PLACEHOLDER_REPLACE_WITH_APPLICATION_SECRET"
}
```

## Running the sample

To run this example from the command line once the `appsettings.json` is configured, run

```shell
python program.py
```

---

Tested against Python 3.9.5
For the OCS Assets samples page [ReadMe](https://github.com/osisoft/OSI-Samples-OCS/blob/main/docs/ASSETS.md)  
For the main OCS samples page [ReadMe](https://github.com/osisoft/OSI-Samples-OCS)  
For the main OSIsoft samples page [ReadMe](https://github.com/osisoft/OSI-Samples)
