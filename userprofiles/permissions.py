from rest_framework import permissions


class IsAuthenticatedOrWriteOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        write_methods = ["POST", ]

        return (
            request.method in write_methods or
            request.user and
            request.user.is_authenticated()
        )