# Database Design

## Contact Entity Structure
### Required Fields
- **name**- Name/surname/patronymic
- **communication_channels** - At least one of:
  - phone number
  - email
  - telegram
  - vk
  - facebook
  - instagram

### Optional Fields
- secondary_name
- birthday
- workplace
- address
- notes

## Validation Rules
| Field            | Type                  | Unique | Requirement       | Description |
|------------------|-----------------------|--------|-------------------|-------------|
| id               | int                   | +      |                   |             |
| name             | string                | -      | max 100 symbols   |             |