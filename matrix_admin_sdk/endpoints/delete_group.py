from .endpoint import Endpoint


class DeleteGroup(Endpoint):
    """
    Delete a group.
    """

    async def delete(self, group_id) -> None:
        """
        This API lets a server admin delete a local group.
        Doing so will kick all users out of the group so that their
        clients will correctly handle the group being deleted.
        Args:
            group_id: The group ID to delete.
        """
        url = f"/_synapse/admin/v1/delete_group/{group_id}"
        await self.admin_client.post(url, data={})
