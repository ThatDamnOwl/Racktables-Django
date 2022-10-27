from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('pk','oldid','username','realname','user')

class UserConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserConfig
        fields = ('pk','user','varname','varvalue')

class MoleculeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Molecule
        fields = ('pk','oldid','description')

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('pk','oldid','name','hasproblems','comment','parentlocation')

class RowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Row
        fields = ('pk','oldid','name','location')

class RackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rack
        fields = ('pk','oldid','name','assetno','hasproblems','comment','height','position','row')

class AtomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atom
        fields = ('pk','molecule','rack','unit_no','xaxis','yaxis','zaxis')

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = ('pk','oldid','attribute_type','name')

class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('pk','oldid','sticky','name')

class DictionarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dictionary
        fields = ('pk','chapter','oldid','sticky','value')

class ObjectTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectType
        fields = ('pk','name','oldid','sticky')

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = ('pk','oldid','name','label','objecttype','assetno','hasproblems','comment','parentobject')

class AttributeMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeMap
        fields = ('pk','attribute','objecttype','chapter','sticky')

class AttributeValueStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValueString
        fields = ('pk','parentobject','attributemap','value')

class AttributeValueIntSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValueInt
        fields = ('pk','parentobject','attributemap','value')

class AttributeValueFloatSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValueFloat
        fields = ('pk','parentobject','attributemap','value')

class AttributeValueDictSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValueDict
        fields = ('pk','parentobject','attributemap','dictionaryvalue')

class AttributeValueDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeValueDate
        fields = ('pk','parentobject','attributemap','value')

class IPv4AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4Address
        fields = ('pk','ip','oldip','name','comment','reserved')

class IPv4VSSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4VS
        fields = ('pk','oldid','vip','oldvip','vport','protocol')

class IPv4AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4Allocation
        fields = ('pk','parentobject','ip','name','alloctype')

class IPv4RSPoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4RSPool
        fields = ('pk','oldid','name','vsconfig','rsconfig')

class IPv4RSSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4RS
        fields = ('pk','oldid','inservice','rsip','oldrsip','rsport','rspool','rsconfig','comment')

class IPv4LBSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4LB
        fields = ('pk','parentobject','parentipv4rspool','parentipv4vs','prio','vsconfig','rsconfig')

class IPv4LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4Log
        fields = ('pk','oldid','ip','date','user','message')

class IPv4NATSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4NAT
        fields = ('pk','parentobject','protocol','localip','localport','remoteip','remoteport','description')

class IPv4NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv4Network
        fields = ('pk','oldid','ip','oldip','mask','name','comment')

class IPv6AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv6Address
        fields = ('pk','ip','oldip','name','comment','reserved')

class IPv6AllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv6Allocation
        fields = ('pk','parentobject','ip','name','alloctype')

class IPv6LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv6Log
        fields = ('pk','oldid','ip','date','user','message')

class IPv6NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = IPv6Network
        fields = ('pk','oldid','ip','oldip','mask','lastip','oldlastip','name','comment')

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = ('pk','name','value','vartype','nullable','hidden','userdefined','description')

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('pk','oldid','name','filetype','size','created','modified','accessed','thumbnail','content','comment')

class FileLinkIPv4NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkIPv4Network
        fields = ('pk','oldid','parent','file')

class FileLinkIPv4RSPoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkIPv4RSPool
        fields = ('pk','oldid','parent','file')

class FileLinkIPv4VSSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkIPv4VS
        fields = ('pk','oldid','parent','file')

class FileLinkIPv6NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkIPv6Network
        fields = ('pk','oldid','parent','file')

class FileLinkLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkLocation
        fields = ('pk','oldid','parent','file')

class FileLinkObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkObject
        fields = ('pk','oldid','parent','file')

class FileLinkRackSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkRack
        fields = ('pk','oldid','parent','file')

class FileLinkRowSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkRow
        fields = ('pk','oldid','parent','file')

class FileLinkUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileLinkUser
        fields = ('pk','oldid','parent','file')

class MountOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MountOperation
        fields = ('pk','oldid','changedobject','changedtime','user','old_molecule','new_molecule','comment')

class ObjectHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectHistory
        fields = ('pk','oldeventid','oldid','name','label','changedobject','assetno','changedtime','user','hasproblems','comment')

class ObjectLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectLog
        fields = ('pk','oldid','parentobject','user','date','content')

class PatchCableConnectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatchCableConnector
        fields = ('pk','oldid','defaultvalue','connectorname')

class PatchCableTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatchCableType
        fields = ('pk','oldid','defaultvalue','cabletype')

class PatchCableConnectorCompatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatchCableConnectorCompat
        fields = ('pk','cabletype','connector')

class PatchCableHeapSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatchCableHeap
        fields = ('pk','oldid','amount','colour','length','end1','end2','cabletype','description')

class PatchCableHeapLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatchCableHeapLog
        fields = ('pk','oldid','heap','date','user','comment')

class PluginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plugin
        fields = ('pk','name','longname','version','homeurl','state')

class PortInnerInterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortInnerInterface
        fields = ('pk','oldid','name')

class PortOuterInterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortOuterInterface
        fields = ('pk','oldid','name')

class PatchCableOIFCompatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatchCableOIFCompat
        fields = ('pk','cabletype','interfacetype')

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = ('pk','oldid','parentobject','name','label','comment','l2address','innerinterface','outerinterface','patch','attachedport')

class VLANDomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = VLANDomain
        fields = ('pk','oldid','parentdomain','description')

class VLANDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VLANDescription
        fields = ('pk','domain','vlan','vlantype','description')

class VLANIPv4Serializer(serializers.ModelSerializer):
    class Meta:
        model = VLANIPv4
        fields = ('pk','vlan','ipv4net')

class VLANIPv6Serializer(serializers.ModelSerializer):
    class Meta:
        model = VLANIPv6
        fields = ('pk','vlan','ipv6network')

class PortAllowedVLANSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortAllowedVLAN
        fields = ('pk','port','vlan','native')

class PortCompatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortCompat
        fields = ('pk','port1','port2')

class PortInterfaceCompatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortInterfaceCompat
        fields = ('pk','portinnerinterface','portouterinterface')

class PortLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortLog
        fields = ('pk','oldid','port','date','user','comment')

class PortVLANModeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortVLANMode
        fields = ('pk','port','trunk')

class RackObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RackObject
        fields = ('pk','oldid','name','label','objecttype','assetno','linkedobject','hasproblems','comment')

class RackSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RackSpace
        fields = ('pk','rack','unitno','atom','state','parentobject')

class RackThumbnailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RackThumbnail
        fields = ('pk','rack','data')

class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = ('pk','name','content')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('pk','oldid','parenttag','assignable','name','colour','description')

class TagFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagFile
        fields = ('pk','file','tag','user','date')

class TagIPv4NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagIPv4Network
        fields = ('pk','ipv4net','tag','user','date')

class TagIPv4RSPoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagIPv4RSPool
        fields = ('pk','ipv4rspool','tag','user','date')

class TagIPv4VSSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagIPv4VS
        fields = ('pk','ipv4vs','tag','user','date')

class TagIPv6NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagIPv6Network
        fields = ('pk','ipv6network','tag','user','date')

class TagLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagLocation
        fields = ('pk','location','tag','user','date')

class TagObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagObject
        fields = ('pk','object','tag','user','date')

class TagRackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagRack
        fields = ('pk','rack','tag','user','date')

class VLANSTRuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = VLANSTRule
        fields = ('pk','oldid','rulenumber','portpcre','portrole','vlans','description')

class VLANSwitchTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = VLANSwitchTemplate
        fields = ('pk','oldid','revision','description','modifiedby')

class VLANSwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = VLANSwitch
        fields = ('pk','parentobject','domain','template','revision','lasterror','lasterroroccured','changed','pushstarted','pushended')

class VLANValidIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = VLANValidID
        fields = ('pk','vlanid')

class VSSerializer(serializers.ModelSerializer):
    class Meta:
        model = VS
        fields = ('pk','oldid','name','vsconfig','rsconfig')

class VSEnabledIPsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VSEnabledIPs
        fields = ('pk','parentobject','parentvs','rspool','vip')

class VSEnabledPortsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VSEnabledPorts
        fields = ('pk','parentobject','parentvs','protocol','rspool','port')

class VSIPsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VSIPs
        fields = ('pk','parentvs','ipv4address')


class VSPortsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VSPorts
        fields = ('pk','parentvs','protocol','port')