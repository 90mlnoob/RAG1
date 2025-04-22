# SOP: Create a New Merchant

## Description

This SOP explains how to create a new merchant account in the system.

## Manual Steps

1. Log in to the Merchant Admin Portal.
2. Click on “Create New Merchant”.
3. Fill in the merchant’s business details, contact info, and settlement preferences.
4. Submit the form and note the generated Merchant ID.

## API Alternative

**Endpoint**: `createMerchant`  
**Method**: `POST`  
**Payload Format**:

```json
{
  "business_name": "<BUSINESS_NAME>",
  "contact_email": "<EMAIL>",
  "settlement_account": "<ACCOUNT_DETAILS>"
}
```

# SOP: View Merchant Details

## Description

This SOP explains how to retrieve the details of a registered merchant.

## Manual Steps

1. Log in to the Merchant Dashboard.
2. Search for the merchant by name or ID.
3. Click on the merchant entry to view details such as business name, status, payment methods, etc.

## API Alternative

**Endpoint**: `getMerchantDetails`  
**Method**: `GET`  
**Query Params**:

```json
{
  "merchant_id": "<MERCHANT_ID>"
}
```

# SOP: Update a Merchant's Name or Address

## Description

This SOP explains how to update the name or address of an existing merchant.

## Manual Steps

1. Navigate to the Merchant Management section.
2. Search and select the merchant to update.
3. Click “Edit” and modify the name or address fields.
4. Save the changes.

## API Alternative

**Endpoint**: `updateMerchantDetails`
**Method**: `PUT`
**Payload Format**:

```json
{
  "merchant_id": "<MERCHANT_ID>",
  "name": "<NEW_NAME>",
  "address": "<NEW_ADDRESS>"
}
```

# SOP: Update Recurring Billing or Auto-Settlement

## Description

This SOP explains how to update the recurring billing or auto-settlement settings for a merchant.

## Manual Steps

1. Log in to the Merchant Dashboard.
2. Navigate to the "Billing Settings" section.
3. Select the merchant whose settings you want to update.
4. Choose "Edit" to update the recurring billing or auto-settlement preferences.
5. Save the changes.

## API Alternative

**Endpoint**: `updateBillingSettings`
**Method**: `PUT`
**Payload Format**:

```json
{
  "merchant_id": "<MERCHANT_ID>",
  "recurring_billing_enabled": <BOOLEAN>,
  "auto_settlement_enabled": <BOOLEAN>
}
```
