# Microsoft Entra ID Configuration

## Steps to Configure Microsoft Entra ID for Power BI

1. **Go to the Microsoft Entra ID portal**:
   - Navigate to the Microsoft Entra ID portal at [https://entra.microsoft.com](https://entra.microsoft.com).

2. **Create a new application for Power BI**:
   - In the left-hand menu, select "App registrations".
   - Click on "New registration".
   - Enter a name for the application (e.g., "Power BI Access").
   - Select the supported account types (e.g., "Accounts in this organizational directory only").
   - Click "Register".

3. **Configure user roles and permissions**:
   - In the application registration, go to "API permissions".
   - Click on "Add a permission".
   - Select "Microsoft Graph".
   - Choose the required permissions (e.g., "User.Read", "Group.Read.All").
   - Click "Add permissions".

4. **Set up Single Sign-On (SSO)**:
   - In the application registration, go to "Authentication".
   - Click on "Add a platform".
   - Select "Web".
   - Enter the redirect URI (e.g., "https://login.microsoftonline.com/common/oauth2/nativeclient").
   - Click "Configure".

5. **Assign users to the application**:
   - In the left-hand menu, select "Enterprise applications".
   - Find and select the newly created application.
   - Go to "Users and groups".
   - Click "Add user/group".
   - Select the users or groups to assign to the application.
   - Click "Assign".

6. **Test the configuration**:
   - Ensure that users can log in to Power BI using their Microsoft Entra ID credentials.
   - Verify that the assigned permissions are working as expected.

