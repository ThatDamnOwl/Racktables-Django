from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('oldid','username','realname','user')

class UserConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConfig
        fields = ('user','varname','varvalue')

class MoleculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Molecule
        fields = ('oldid','description')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('oldid','name','hasproblems','comment','parentlocation')

class RowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Row
        fields = ('oldid','name','location')

class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rack
        fields = ('oldid','name','assetno','hasproblems','comment','height','position','row')

class AtomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atom
        fields = ('molecule','rack','unit_no','xaxis','yaxis','zaxis')

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('oldid','attribute_type','name')

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('oldid','sticky','name')

class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ('chapter','oldid','sticky','value')

class ObjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectType
        fields = ('name','oldid','sticky')

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ('oldid','name','label','objecttype','assetno','hasproblems','comment','parentobject')

class AttributeMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeMap
        fields = ('attribute','objecttype','chapter','sticky')

class AttributeValueStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValueString
        fields = ('parentobject','attributemap','value')

class AttributeValueIntSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValueInt
        fields = ('parentobject','attributemap','value')

class AttributeValueFloatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValueFloat
        fields = ('parentobject','attributemap','value')

class AttributeValueDictSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValueDict
        fields = ('parentobject','attributemap','dictionaryvalue')

class AttributeValueDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValueDate
        fields = ('parentobject','attributemap','value')

class IPv4AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4Address
        fields = ('ip','oldip','name','comment','reserved')

class IPv4VSSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4VS
        fields = ('oldid','vip','oldvip','vport','protocol')

class IPv4AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4Allocation
        fields = ('parentobject','ip','name','alloctype')

class IPv4RSPoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4RSPool
        fields = ('oldid','name','vsconfig','rsconfig')

class IPv4RSSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4RS
        fields = ('oldid','inservice','rsip','oldrsip','rsport','rspool','rsconfig','comment')

class IPv4LBSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4LB
        fields = ('parentobject','parentipv4rspool','parentipv4vs','prio','vsconfig','rsconfig')

class IPv4LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4Log
        fields = ('oldid','ip','date','user','message')

class IPv4NATSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4NAT
        fields = ('parentobject','protocol','localip','localport','remoteip','remoteport','description')

class IPv4NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4Network
        fields = ('oldid','ip','oldip','mask','name','comment')

class IPv6AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv6Address
        fields = ('ip','oldip','name','comment','reserved')

class IPv6AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv6Allocation
        fields = ('parentobject','ip','name','alloctype')

class IPv6LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv6Log
        fields = ('oldid','ip','date','user','message')

class IPv6NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv6Network
        fields = ('oldid','ip','oldip','mask','lastip','oldlastip','name','comment')

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = ('name','value','vartype','nullable','hidden','userdefined','description')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('oldid','name','filetype','size','created','modified','accessed','thumbnail','content','comment')

class FileLinkIPv4NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkIPv4Network
        fields = ('oldid','parent','file')

class FileLinkIPv4RSPoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkIPv4RSPool
        fields = ('oldid','parent','file')

class FileLinkIPv4VSSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkIPv4VS
        fields = ('oldid','parent','file')

class FileLinkIPv6NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkIPv6Network
        fields = ('oldid','parent','file')

class FileLinkLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkLocation
        fields = ('oldid','parent','file')

class FileLinkObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkObject
        fields = ('oldid','parent','file')

class FileLinkRackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkRack
        fields = ('oldid','parent','file')

class FileLinkRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkRow
        fields = ('oldid','parent','file')

class FileLinkUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkUser
        fields = ('oldid','parent','file')

class MountOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountOperation
        fields = ('oldid','changedobject','changedtime','user','old_molecule','new_molecule','comment')

class ObjectHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectHistory
        fields = ('oldeventid','oldid','name','label','changedobject','assetno','changedtime','user','hasproblems','comment')

class ObjectLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectLog
        fields = ('oldid','parentobject','user','date','content')

class PatchCableConnectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatchCableConnector
        fields = ('oldid','defaultvalue','connectorname')

class PatchCableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatchCableType
        fields = ('oldid','defaultvalue','cabletype')

class PatchCableConnectorCompatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatchCableConnectorCompat
        fields = ('cabletype','connector')

class PatchCableHeapSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatchCableHeap
        fields = ('oldid','amount','colour','length','end1','end2','cabletype','description')

class PatchCableHeapLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatchCableHeapLog
        fields = ('oldid','heap','date','user','comment')

class PluginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plugin
        fields = ('name','longname','version','homeurl','state')

class PortInnerInterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortInnerInterface
        fields = ('oldid','name')

class PortOuterInterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortOuterInterface
        fields = ('oldid','name')

class PatchCableOIFCompatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatchCableOIFCompat
        fields = ('cabletype','interfacetype')

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = ('oldid','parentobject','name','label','comment','l2address','innerinterface','outerinterface','patch','attachedport')

class VLANDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = VLANDomain
        fields = ('oldid','parentdomain','description')

class VLANDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VLANDescription
        fields = ('domain','vlan','vlantype','description')

class VLANIPv4Serializer(serializers.ModelSerializer):
    class Meta:
        model = VLANIPv4
        fields = ('vlan','ipv4net')

class VLANIPv6Serializer(serializers.ModelSerializer):
    class Meta:
        model = VLANIPv6
        fields = ('vlan','ipv6network')

class PortAllowedVLANSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortAllowedVLAN
        fields = ('port','vlan','native')

class PortCompatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortCompat
        fields = ('port1','port2')

class PortInterfaceCompatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortInterfaceCompat
        fields = ('portinnerinterface','portouterinterface')

class PortLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortLog
        fields = ('oldid','port','date','user','comment')

class PortVLANModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortVLANMode
        fields = ('port','trunk')

class RackObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RackObject
        fields = ('oldid','name','label','objecttype','assetno','linkedobject','hasproblems','comment')

class RackSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RackSpace
        fields = ('rack','unitno','atom','state','parentobject')

class RackThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RackThumbnail
        fields = ('rack','data')

class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = ('name','content')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('oldid','parenttag','assignable','name','colour','description')

class TagFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagFile
        fields = ('file','tag','user','date')

class TagIPv4NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagIPv4Network
        fields = ('ipv4net','tag','user','date')

class TagIPv4RSPoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagIPv4RSPool
        fields = ('ipv4rspool','tag','user','date')

class TagIPv4VSSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagIPv4VS
        fields = ('ipv4vs','tag','user','date')

class TagIPv6NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagIPv6Network
        fields = ('ipv6network','tag','user','date')

class TagLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagLocation
        fields = ('location','tag','user','date')

class TagObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagObject
        fields = ('object','tag','user','date')

class TagRackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagRack
        fields = ('rack','tag','user','date')

class VLANSTRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VLANSTRule
        fields = ('oldid','rulenumber','portpcre','portrole','vlans','description')

class VLANSwitchTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VLANSwitchTemplate
        fields = ('oldid','revision','description','modifiedby')

class VLANSwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = VLANSwitch
        fields = ('parentobject','domain','template','revision','lasterror','lasterroroccured','changed','pushstarted','pushended')

class VLANValidIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = VLANValidID
        fields = ('vlanid')

class VSSerializer(serializers.ModelSerializer):
    class Meta:
        model = VS
        fields = ('oldid','name','vsconfig','rsconfig')

class VSEnabledIPsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VSEnabledIPs
        fields = ('parentobject','parentvs','rspool','vip')

class VSEnabledPortsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VSEnabledPorts
        fields = ('parentobject','parentvs','protocol','rspool','port')

class VSIPsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VSIPs
        fields = ('parentvs','ipv4address')


class VSPortsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VSPorts
        fields = ('parentvs','protocol','port')