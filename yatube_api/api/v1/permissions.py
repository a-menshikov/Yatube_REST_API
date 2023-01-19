from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Даёт доступ неавтору только к GET/OPTIONS/HEAD."""

    message = 'Данный запрос доступен только автору объекта'

    def has_object_permission(self, request, view, obj):
        """Проверка на запросы к объекту
        Для безопасных методов всегда True."""
        return (obj.author == request.user
                or request.method in permissions.SAFE_METHODS)
