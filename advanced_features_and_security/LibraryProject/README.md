# Permissions and Groups Setup

## Custom Permissions
Defined in `blog/models.py` (Article model):
- can_view: Can view articles
- can_create: Can create articles
- can_edit: Can edit articles
- can_delete: Can delete articles

## Groups
Created via `setup_groups` management command:
- **Viewers** → can_view
- **Editors** → can_view, can_create, can_edit
- **Admins** → can_view, can_create, can_edit, can_delete

## Enforcing Permissions
- Views are protected using `@permission_required` decorators in `blog/views.py`.
- Example: `@permission_required("blog.can_edit")` ensures only Editors/Admins can edit.

## Testing
1. Create users and assign them to groups in Django Admin.
2. Try accessing different views.
3. Permissions will raise `403 Forbidden` if unauthorized.
