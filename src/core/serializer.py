from rest_framework import serializers

from core.sotrage import Storage

class TaskSerializer(serializers.Serializer):

    def __init__(self, storage: Storage, **kwargs):
        super().__init__(self, **kwargs)
        self._storage = storage
        
    id = serializers.UUIDField(read_only=True)
    title = serializers.CharField()
    context = serializers.CharField(required=False)
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)

    def save(self, validated_data):
        """
        Create and return a new `Task` instance, given the validated data.
        """
        print(validated_data)
        return self._storage.save(validated_data)