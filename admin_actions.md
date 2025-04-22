# SOP: Generate Bearer Access Token for API Access/authorization/authentication

## Purpose

Obtain a bearer access token to authenticate and authorize API calls for secured endpoints.
Required as a pre-requisite for all API calls.

## Procedure

1. Make a POST request to `https://auth.company.com/oauth2/token`.
2. Set headers:
   - `Content-Type`: `application/x-www-form-urlencoded`
3. Send body parameters:
   - `grant_type`: `client_credentials`
   - `client_id`: Saurav
   - `client_secret`: Saurav234
4. On success, extract the `access_token` from the response.
5. Use the token in future API requests by setting:
   - Header: `Authorization: Bearer <access_token>`
