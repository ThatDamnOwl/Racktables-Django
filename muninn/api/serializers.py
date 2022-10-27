from django.contrib.auth.models import User, Group
from rest_framework import serializers
        
class UserAccountSerializer (serializer.ModelSerializer):

    class Meta:UserAccount
        model = 
        fields = ('')

class UserConfigSerializer (serializer.ModelSerializer):

    class Meta:
        model = UserConfig
        fields = ('')

class MoleculeSerializer (serializer.ModelSerializer):

    class Meta:
        model = Molecule
        fields = ('')

class LocationSerializer (serializer.ModelSerializer):

    class Meta:
        model = Location
        fields = ('')

class RowSerializer (serializer.ModelSerializer):

    class Meta:
        model = Row
        fields = ('')

class RackSerializer (serializer.ModelSerializer):

    class Meta:
        model = Rack
        fields = ('')

class AtomSerializer (serializer.ModelSerializer):

    class Meta:
        model = Atom
        fields = ('')

class AttributeSerializer (serializer.ModelSerializer):

    class Meta:
        model = Attribute
        fields = ('')

class ChapterSerializer (serializer.ModelSerializer):

    class Meta:
        model = Chapter
        fields = ('')

class DictionarySerializer (serializer.ModelSerializer):

    class Meta:
        model = Dictionary
        fields = ('')

class ObjectTypeSerializer (serializer.ModelSerializer):

    class Meta:
        model = ObjectType
        fields = ('')

class ObjectSerializer (serializer.ModelSerializer):

    class Meta:
        model = Object
        fields = ('')

class AttributeMapSerializer (serializer.ModelSerializer):

    class Meta:
        model = AttributeMap
        fields = ('')

class AttributeValueStrinSerializer (serializer.ModelSerializer):

    class Meta:
        model = AttributeValueStrin
        fields = ('')

class AttributeValueIntSerializer (serializer.ModelSerializer):

    class Meta:
        model = AttributeValueInt
        fields = ('')

class AttributeValueFloatSerializer (serializer.ModelSerializer):

    class Meta:
        model = AttributeValueFloat
        fields = ('')

class AttributeValueDictSerializer (serializer.ModelSerializer):

    class Meta:
        model = AttributeValueDict
        fields = ('')

class AttributeValueDateSerializer (serializer.ModelSerializer):

    class Meta:
        model = AttributeValueDate
        fields = ('')

class IPv4AddressSerializer (serializer.ModelSerializer):

    class Meta:
        model = IPv4Address
        fields = ('')

class IPv4VSSerializer (serializer.ModelSerializer):

    class Meta:
        model = IPv4VS
        fields = ('')

class IPv4AllocationSerializer (serializer.ModelSerializer):

    class Meta:
        model = IPv4Allocation
        fields = ('')

class IPv4RSPoolSerializer (serializer.ModelSerializer):

    class Meta:
        model = IPv4RSPool
        fields = ('')

class IPv4RSSerializer (serializer.ModelSerializer):

    class Meta:
        model = IPv4RS
        fields = ('')

class IPv4LBSerializer (serializer.ModelSerializer):

    class Meta:
        model = IPv4LB
        fields = ('')

class IPv4LogSerializer (serializer.ModelSerializer):

    class Meta:
        model = IPv4Log
        fields = ('')

class IPv4NATSerializer (serializer.ModelSerializer):

    class Meta:
        model = IPv4NAT
        fields = ('')

class IPv4NetworkSerializer (serializer.ModelSerializer):

    class Meta:
        model = IPv4Network
        fields = ('')

class IPv6AddressSerializer (serializer.ModelSerializer):

    class Meta:
        model = IPv6Address
        fields = ('')

class IPv6AllocationSerializer (serializer.ModelSerializer):

    class Meta:
        model = IPv6Allocation
        fields = ('')

class IPv6LogSerializer (serializer.ModelSerializer):

    class Meta:
        model = IPv6Log
        fields = ('')

class IPv6NetworkSerializer (serializer.ModelSerializer):

    class Meta:
        model = IPv6Network
        fields = ('')

class ConfigSerializer (serializer.ModelSerializer):

    class Meta:
        model = Config
        fields = ('')

class FileSerializer (serializer.ModelSerializer):

    class Meta:
        model = File
        fields = ('')

class FileLinkIPv4NetworkSerializer (serializer.ModelSerializer):

    class Meta:
        model = FileLinkIPv4Network
        fields = ('')

class FileLinkIPv4RSPoolSerializer (serializer.ModelSerializer):

    class Meta:
        model = FileLinkIPv4RSPool
        fields = ('')

class FileLinkIPv4VSSerializer (serializer.ModelSerializer):

    class Meta:
        model = FileLinkIPv4VS
        fields = ('')

class FileLinkIPv6NetworkSerializer (serializer.ModelSerializer):

    class Meta:
        model = FileLinkIPv6Network
        fields = ('')

class FileLinkLocationSerializer (serializer.ModelSerializer):

    class Meta:
        model = FileLinkLocation
        fields = ('')

class FileLinkObjectSerializer (serializer.ModelSerializer):

    class Meta:
        model = FileLinkObject
        fields = ('')

class FileLinkRackSerializer (serializer.ModelSerializer):

    class Meta:
        model = FileLinkRack
        fields = ('')

class FileLinkRowSerializer (serializer.ModelSerializer):

    class Meta:
        model = FileLinkRow
        fields = ('')

class FileLinkUserSerializer (serializer.ModelSerializer):

    class Meta:
        model = FileLinkUser
        fields = ('')

class MountOperationSerializer (serializer.ModelSerializer):

    class Meta:
        model = MountOperation
        fields = ('')

class ObjectHistorySerializer (serializer.ModelSerializer):

    class Meta:
        model = ObjectHistory
        fields = ('')

class ObjectLogSerializer (serializer.ModelSerializer):

    class Meta:
        model = ObjectLog
        fields = ('')

class PatchCableConnectorSerializer (serializer.ModelSerializer):

    class Meta:
        model = PatchCableConnector
        fields = ('')

class PatchCableTypeSerializer (serializer.ModelSerializer):

    class Meta:
        model = PatchCableType
        fields = ('')

class PatchCableConnectorSerializer (serializer.ModelSerializer):

    class Meta:
        model = PatchCableConnector
        fields = ('')

class PatchCableHeapSerializer (serializer.ModelSerializer):

    class Meta:
        model = PatchCableHeap
        fields = ('')

class PatchCableHeapLogSerializer (serializer.ModelSerializer):

    class Meta:
        model = PatchCableHeapLog
        fields = ('')

class PluginSerializer (serializer.ModelSerializer):

    class Meta:
        model = Plugin
        fields = ('')

class PortInnerInterfaceSerializer (serializer.ModelSerializer):

    class Meta:
        model = PortInnerInterface
        fields = ('')

class PortOuterInterfaceSerializer (serializer.ModelSerializer):

    class Meta:
        model = PortOuterInterface
        fields = ('')

class PatchCableOIFCompatSerializer (serializer.ModelSerializer):

    class Meta:
        model = PatchCableOIFCompat
        fields = ('')

class PortSerializer (serializer.ModelSerializer):

    class Meta:
        model = Port
        fields = ('')

class VLANDomainSerializer (serializer.ModelSerializer):

    class Meta:
        model = VLANDomain
        fields = ('')

class VLANDescriptionSerializer (serializer.ModelSerializer):

    class Meta:
        model = VLANDescription
        fields = ('')

class VLANIPv4Serializer (serializer.ModelSerializer):

    class Meta:
        model = VLANIPv4
        fields = ('')

class VLANIPv6Serializer (serializer.ModelSerializer):

    class Meta:
        model = VLANIPv6
        fields = ('')

class PortAllowedVLANSerializer (serializer.ModelSerializer):

    class Meta:
        model = PortAllowedVLAN
        fields = ('')

class PortCompatSerializer (serializer.ModelSerializer):

    class Meta:
        model = PortCompat
        fields = ('')

class PortInterfaceCompatSerializer (serializer.ModelSerializer):

    class Meta:
        model = PortInterfaceCompat
        fields = ('')

class PortLogSerializer (serializer.ModelSerializer):

    class Meta:
        model = PortLog
        fields = ('')

class PortVLANModeSerializer (serializer.ModelSerializer):

    class Meta:
        model = PortVLANMode
        fields = ('')

class RackObjectSerializer (serializer.ModelSerializer):

    class Meta:
        model = RackObject
        fields = ('')

class RackSpaceSerializer (serializer.ModelSerializer):

    class Meta:
        model = RackSpace
        fields = ('')

class RackThumbnailSerializer (serializer.ModelSerializer):

    class Meta:
        model = RackThumbnail
        fields = ('')

class ScriptSerializer (serializer.ModelSerializer):

    class Meta:
        model = Script
        fields = ('')

class TagSerializer (serializer.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('')

class TagFileSerializer (serializer.ModelSerializer):

    class Meta:
        model = TagFile
        fields = ('')

class TagIPv4NetworkSerializer (serializer.ModelSerializer):

    class Meta:
        model = TagIPv4Network
        fields = ('')

class TagIPv4RSPoolSerializer (serializer.ModelSerializer):

    class Meta:
        model = TagIPv4RSPool
        fields = ('')

class TagIPv4VSSerializer (serializer.ModelSerializer):

    class Meta:
        model = TagIPv4VS
        fields = ('')

class TagIPv6NetworkSerializer (serializer.ModelSerializer):

    class Meta:
        model = TagIPv6Network
        fields = ('')

class TagLocationSerializer (serializer.ModelSerializer):

    class Meta:
        model = TagLocation
        fields = ('')

class TagObjectSerializer (serializer.ModelSerializer):

    class Meta:
        model = TagObject
        fields = ('')

class TagRackSerializer (serializer.ModelSerializer):

    class Meta:
        model = TagRack
        fields = ('')

class VLANSTRuleSerializer (serializer.ModelSerializer):

    class Meta:
        model = VLANSTRule
        fields = ('')

class VLANSwitchTemplateSerializer (serializer.ModelSerializer):

    class Meta:
        model = VLANSwitchTemplate
        fields = ('')

class VLANSwitchSerializer (serializer.ModelSerializer):

    class Meta:
        model = VLANSwitch
        fields = ('')

class VLANValidIDSerializer (serializer.ModelSerializer):

    class Meta:
        model = VLANValidID
        fields = ('')

class VSSerializer (serializer.ModelSerializer):

    class Meta:
        model = VS
        fields = ('')

class VSEnabledIPsSerializer (serializer.ModelSerializer):

    class Meta:
        model = VSEnabledIPs
        fields = ('')

class VSEnabledPortsSerializer (serializer.ModelSerializer):

    class Meta:
        model = VSEnabledPorts
        fields = ('')

class VSIPsSerializer (serializer.ModelSerializer):

    class Meta:
        model = VSIPs
        fields = ('')

class VSPortsSerializer (serializer.ModelSerializer):

    class Meta:
        model = VSPorts
        fields = ('')
