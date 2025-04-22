# --- File: sops/disable_user_access.md ---

# SOP: Disable VPN Access for Employee

## Purpose

Disable VPN access for an employee.

## Procedure

1. Go to `https://vpnadmin.company.com`
2. Login as admin.
3. Search user by empID.
4. Disable VPN access.
5. Save changes.

---

# SOP: Disable Email Access for Employee

## Purpose

Disable email access for an employee.

## Procedure

1. Go to `https://emailadmin.company.com`
2. Search empID.
3. Disable email access.
4. Click apply.

---

# SOP: Reset Employee Password

## Purpose

Reset password for a locked employee account.

## Procedure

1. Navigate to `https://passwordreset.company.com`
2. Enter empID in search.
3. Click 'Reset Password'.
4. Generate new password.
5. Communicate new credentials securely to user.

---

# SOP: Add User to DL

## Purpose

Add employee to mailing list (Distribution List).

## Procedure

1. Open `https://emailadmin.company.com`
2. Search for Distribution List.
3. Select 'Members' tab.
4. Click 'Add Member'.
5. Enter empID/email.
6. Confirm addition.

---

# SOP: Terminate AWS IAM Access

## Purpose

Revoke AWS console and programmatic access for a user.

## Procedure

1. Login to AWS Console.
2. Go to IAM > Users.
3. Search by empID.
4. Detach all policies.
5. Deactivate access keys.
6. Delete user.

---

# SOP: Raise Incident with Network Team

## Purpose

Escalate network issue to relevant team.

## Procedure

1. Open `https://itportal.company.com`
2. Click 'Raise New Ticket'.
3. Fill category as 'Network'.
4. Provide description.
5. Attach screenshots.
6. Submit ticket.

# SOP: Terminate/Deactivate an employee/user account via Internal API

## Purpose

To deactivate/terminate an employee/user's account using the internal API.
pre-requisite: obtain the bearer access token from SOP: Generate Bearer Token for API Access/authorization/authentication

## Procedure

1. Prepare API endpoint: `https://internal-api.company.com/v1/users/deactivate`
2. Use HTTP `POST` method.
3. Include authorization header:
   - Key: `Authorization`
   - Value: `Bearer <access_token>`
4. Set Content-Type header to `application/json`.
5. In the JSON body, include:
   ```json
   {
     "empID": "<employee id>",
     "reason": "<reason for deactivation or termination>"
   }
   ```
