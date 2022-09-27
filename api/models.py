from django.db import models
from django.contrib.auth.models import User, Group
from . import bitflags, choices
# Create your models here.

class UserAccount(models.Model):
	oldid = models.IntegerField()
	username = models.TextField(64)
	realname = models.TextField(64)
	old_passhash = models.TextField(40)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class UserConfig(models.Model):
	user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
	varname = models.TextField(32)
	varvalue = models.TextField()	

class Molecule(models.Model):
	oldid = models.IntegerField()
	description = models.TextField(255)

class Location(models.Model):
	oldid = models.IntegerField()
	name = models.TextField(255)
	hasproblems = models.BinaryField()
	comment = models.TextField()
	parentlocation = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

class Row(models.Model):
	oldid = models.IntegerField()
	name = models.TextField(255)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)

class Rack(models.Model):
	oldid = models.IntegerField()
	name = models.TextField(255)
	assetno = models.TextField(64)
	hasproblems = models.BooleanField()
	comment = models.TextField()
	height = models.SmallIntegerField()
	position = models.SmallIntegerField()
	row = models.ForeignKey(Row, on_delete=models.CASCADE)	

class Atom(models.Model):
	molecule = models.ForeignKey(Molecule, on_delete=models.CASCADE)
	rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
	unit_no = models.IntegerField()
	xaxis = bitflags.BitFlagField(choices=choices.XAxis)
	yaxis = bitflags.BitFlagField(choices=choices.YAxis)
	zaxis = bitflags.BitFlagField(choices=choices.ZAxis)

class Attribute(models.Model):
	oldid = models.IntegerField()
	attribute_type = models.IntegerField(choices=choices.ValueType.choices)
	name = models.TextField(64)

class Chapter(models.Model):
	oldid = models.IntegerField()
	sticky = models.BooleanField()
	name = models.TextField(255)

class Dictionary(models.Model):
	chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
	oldid = models.IntegerField()
	sticky = models.BooleanField()
	value = models.TextField(255)
	
class ObjectType(models.Model):
	name = models.TextField()
	oldid = models.IntegerField()
	sticky = models.BooleanField()

class Object(models.Model):
	oldid = models.IntegerField()
	name = models.TextField(255)
	label = models.TextField(255)
	objecttype = models.ForeignKey(ObjectType, on_delete=models.CASCADE)
	assetno = models.TextField(64)
	hasproblems = models.BooleanField()
	comment = models.TextField()
	parentobject = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

class AttributeMap(models.Model):
	attribute = models.ForeignKey(Attribute, on_delete=models.CASCADE)
	objecttype = models.ForeignKey(ObjectType, on_delete=models.CASCADE)
	chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, blank=True, null=True)
	sticky = models.BooleanField()

class AttributeValueString(models.Model):
	parentobject = models.ForeignKey(Object, on_delete=models.CASCADE)
	attributemap = models.ForeignKey(AttributeMap, on_delete=models.CASCADE)
	value = models.TextField(255, blank=True, null=True)

class AttributeValueInt(models.Model):
	parentobject = models.ForeignKey(Object, on_delete=models.CASCADE)
	attributemap = models.ForeignKey(AttributeMap, on_delete=models.CASCADE)
	value = models.IntegerField(blank=True, null=True)

class AttributeValueFloat(models.Model):
	parentobject = models.ForeignKey(Object, on_delete=models.CASCADE)
	attributemap = models.ForeignKey(AttributeMap, on_delete=models.CASCADE)
	value = models.FloatField(blank=True, null=True)

class AttributeValueDict(models.Model):
	parentobject = models.ForeignKey(Object, on_delete=models.CASCADE)
	attributemap = models.ForeignKey(AttributeMap, on_delete=models.CASCADE)
	dictionaryvalue = models.ForeignKey(Dictionary, on_delete=models.CASCADE)

class AttributeValueDate(models.Model):
	parentobject = models.ForeignKey(Object, on_delete=models.CASCADE)
	attributemap = models.ForeignKey(AttributeMap, on_delete=models.CASCADE)
	value = models.DateField(blank=True, null=True)

class IPv4Address(models.Model):
	ip = models.GenericIPAddressField(unpack_ipv4=True)
	oldip = models.PositiveBigIntegerField()
	name = models.TextField(255)
	comment = models.TextField(10000)
	reserved = models.BooleanField()

class IPv4VS(models.Model):
	oldid = models.IntegerField()
	vip = models.ForeignKey(IPv4Address, on_delete=models.CASCADE)
	oldvip = models.BinaryField(16)
	vport = models.SmallIntegerField()
	protocol = bitflags.BitFlagField(choices=choices.Protocol)
	name = models.TextField(255)
	vsconfig = models.TextField()
	rsconfig = models.TextField()

class IPv4Allocation(models.Model):
	parentobject = models.ForeignKey(Object, on_delete=models.CASCADE)
	ip = models.ForeignKey(IPv4Address, on_delete=models.CASCADE)
	name = models.TextField(255)
	alloctype = models.IntegerField(choices=choices.AllocType.choices)

class IPv4RSPool(models.Model):
	oldid = models.IntegerField()
	name = models.TextField(255)
	vsconfig = models.TextField()
	rsconfig = models.TextField()

class IPv4RS(models.Model):
	oldid = models.IntegerField()
	inservice = models.BooleanField()
	rsip = models.ForeignKey(IPv4Address, on_delete=models.CASCADE)
	oldrsip = models.PositiveBigIntegerField()
	rsport = models.SmallIntegerField()
	rspool = models.ForeignKey(IPv4RSPool, on_delete=models.CASCADE)
	rsconfig = models.TextField()
	comment = models.TextField(255)

class IPv4LB(models.Model):
	parentobject = models.ForeignKey(Object, on_delete=models.CASCADE)
	parentipv4rspool = models.ForeignKey(IPv4RSPool, on_delete=models.CASCADE)
	parentipv4vs = models.ForeignKey(IPv4VS, on_delete=models.CASCADE)
	prio = models.TextField(255)
	vsconfig = models.TextField()
	rsconfig = models.TextField()

class IPv4Log(models.Model):
	oldid = models.IntegerField()
	ip = models.ForeignKey(IPv4Address, on_delete=models.RESTRICT)
	date = models.DateTimeField()
	user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
	message = models.TextField()

class IPv4NAT(models.Model):
	parentobject = models.ForeignKey(Object, on_delete=models.CASCADE)
	protocol = bitflags.BitFlagField(choices=choices.Protocol)
	localip = models.ForeignKey(IPv4Address, on_delete=models.RESTRICT, related_name='nat_local_ip')
	localport = models.IntegerField()
	remoteip = models.ForeignKey(IPv4Address, on_delete=models.RESTRICT, related_name='nat_remote_ip')
	remoteport = models.IntegerField()
	description = models.TextField(255)

class IPv4Network(models.Model):
	oldid = models.IntegerField()
	ip = models.GenericIPAddressField(unpack_ipv4=True)
	oldip = models.PositiveBigIntegerField()
	mask = models.PositiveSmallIntegerField()
	name = models.TextField(255)
	comment = models.TextField()

class IPv6Address(models.Model):
	ip = models.GenericIPAddressField()
	oldip = models.BinaryField(16)
	name = models.TextField(255)
	comment = models.TextField(255)
	reserved = models.BooleanField()

class IPv6Allocation(models.Model):
	parentobject = models.ForeignKey(Object, on_delete=models.CASCADE)
	ip = models.ForeignKey(IPv6Address, on_delete=models.RESTRICT)
	name = models.TextField(255)
	alloctype = models.IntegerField(choices=choices.AllocType.choices)

class IPv6Log(models.Model):
	oldid = models.IntegerField()
	ip = models.ForeignKey(IPv6Address, on_delete=models.RESTRICT)
	date = models.DateTimeField()
	user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
	message = models.TextField()

class IPv6Network(models.Model):
	oldid = models.IntegerField()
	ip = models.GenericIPAddressField()
	oldip = models.BinaryField(16)
	mask = models.PositiveSmallIntegerField()
	lastip = models.GenericIPAddressField()
	oldlastip = models.BinaryField(16)
	name = models.TextField(255)
	comment = models.TextField()

class Config(models.Model):
	name = models.TextField(32)
	value = models.TextField(255)
	vartype = models.IntegerField(choices=choices.ValueType.choices)
	nullable = models.BooleanField()
	hidden = models.BooleanField()
	userdefined = models.BooleanField()
	description = models.TextField(255)

class File(models.Model):
	oldid = models.IntegerField()
	name = models.TextField(255)
	filetype = models.ForeignKey(Dictionary, on_delete=models.RESTRICT)
	size = models.IntegerField()
	created = models.DateTimeField()
	modified = models.DateTimeField()
	accessed = models.DateTimeField()
	thumbnail = models.BinaryField(131072, blank=True, null=True)
	content = models.BinaryField(52428800)
	comment = models.TextField(10000)

class FileLinkIPv4Network(models.Model):
	oldid = models.IntegerField()
	parent = models.ForeignKey(IPv4Network, on_delete=models.CASCADE)
	file = models.ForeignKey(File, on_delete=models.CASCADE)

class FileLinkIPv4RSPool(models.Model):
	oldid = models.IntegerField()
	parent = models.ForeignKey(IPv4RSPool, on_delete=models.CASCADE)
	file = models.ForeignKey(File, on_delete=models.CASCADE)

class FileLinkIPv4VS(models.Model):
	oldid = models.IntegerField()
	parent = models.ForeignKey(IPv4VS, on_delete=models.CASCADE)
	file = models.ForeignKey(File, on_delete=models.CASCADE)

class FileLinkIPv6Network(models.Model):
	oldid = models.IntegerField()
	parent = models.ForeignKey(IPv6Network, on_delete=models.CASCADE)
	file = models.ForeignKey(File, on_delete=models.CASCADE)

class FileLinkLocation(models.Model):
	oldid = models.IntegerField()
	parent = models.ForeignKey(Location, on_delete=models.CASCADE)
	file = models.ForeignKey(File, on_delete=models.CASCADE)

class FileLinkObject(models.Model):
	oldid = models.IntegerField()
	parent = models.ForeignKey(Object, on_delete=models.CASCADE)
	file = models.ForeignKey(File, on_delete=models.CASCADE)

class FileLinkRack(models.Model):
	oldid = models.IntegerField()
	parent = models.ForeignKey(Rack, on_delete=models.CASCADE)
	file = models.ForeignKey(File, on_delete=models.CASCADE)

class FileLinkRow(models.Model):
	oldid = models.IntegerField()
	parent = models.ForeignKey(Row, on_delete=models.CASCADE)
	file = models.ForeignKey(File, on_delete=models.CASCADE)

class FileLinkUser(models.Model):
	oldid = models.IntegerField()
	parent = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
	file = models.ForeignKey(File, on_delete=models.CASCADE)

class MountOperation(models.Model):
	oldid = models.IntegerField()
	changedobject = models.ForeignKey(Object, on_delete=models.SET_NULL, blank=True, null=True)
	changedtime = models.DateTimeField()
	user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
	old_molecule = models.ForeignKey(Molecule, on_delete=models.CASCADE, blank=True, null=True, related_name='old_molecule')
	new_molecule = models.ForeignKey(Molecule, on_delete=models.CASCADE, blank=True, null=True, related_name='new_molecule')
	comment = models.TextField()

class ObjectHistory(models.Model):
	oldid = models.IntegerField()
	changedobject = models.ForeignKey(Object, on_delete=models.CASCADE)
	changedtime = models.DateTimeField()
	user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
	hasproblems = models.BooleanField()
	comment = models.TextField()
	change = models.TextField(100)
	oldvalue = models.TextField()
	

class ObjectLog(models.Model):
	oldid = models.IntegerField()
	parentobject = models.ForeignKey(Object, on_delete=models.CASCADE)
	user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
	date = models.DateTimeField()
	content = models.TextField()

class PatchCableConnector(models.Model):
	oldid = models.IntegerField()
	default = models.BooleanField()
	connectorname = models.TextField(32)

class PatchCableType(models.Model):
	oldid = models.IntegerField()
	default = models.BooleanField()
	cabletype = models.TextField()

class PatchCableConnectorCompat(models.Model):
	cabletype = models.ForeignKey(PatchCableType, on_delete=models.CASCADE)
	connector = models.ForeignKey(PatchCableConnector, on_delete=models.CASCADE)	

class PatchCableHeap(models.Model):
	oldid = models.IntegerField()
	amount = models.IntegerField()
	colour = models.BinaryField(3)
	length = models.IntegerField()
	end1 = models.ForeignKey(PatchCableConnector, on_delete=models.CASCADE, related_name='end1')
	end2 = models.ForeignKey(PatchCableConnector, on_delete=models.CASCADE, related_name='end2')
	cabletype = models.ForeignKey(PatchCableType, on_delete=models.CASCADE)
	description = models.TextField(255)

class PatchCableHeapLog(models.Model):
	oldid = models.IntegerField()
	heap = models.ForeignKey(PatchCableHeap, on_delete=models.CASCADE)
	date = models.DateTimeField()
	user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
	comment = models.TextField()

class Plugin(models.Model):
	name = models.TextField(255)
	longname = models.TextField(255)
	version = models.TextField(64)
	homeurl = models.TextField()
	state = models.BooleanField()

class PortInnerInterface(models.Model):
	oldid = models.IntegerField()
	name = models.TextField(32)		

class PortOuterInterface(models.Model):
	oldid = models.IntegerField()
	name = models.TextField(50)

class PatchCableOIFCompat(models.Model):
	cabletype = models.ForeignKey(PatchCableType, on_delete=models.CASCADE)
	interfacetype = models.ForeignKey(PortInnerInterface, on_delete=models.CASCADE)

class Port(models.Model):
	oldid = models.IntegerField()
	parentobject = models.ForeignKey(Object, on_delete=models.CASCADE)
	name = models.TextField(255)
	label = models.TextField(255)
	comment = models.TextField(255)
	l2address = models.TextField(30)
	innerinterface = models.ForeignKey(PortInnerInterface, on_delete=models.CASCADE, blank=True, null=True)
	outerinterface = models.ForeignKey(PortOuterInterface, on_delete=models.CASCADE)
	patch = models.ForeignKey(PatchCableHeap, on_delete=models.SET_NULL, blank=True, null=True)
	attachedport = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)

class VLANDomain(models.Model):
	oldid = models.IntegerField()
	parentdomain = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
	description = models.TextField(255)

class VLANDescription(models.Model):
	domain = models.ForeignKey(VLANDomain, on_delete=models.CASCADE)
	vlan = models.SmallIntegerField()
	vlantype = models.IntegerField(choices=choices.VLANType.choices)
	description = models.TextField(255)

class VLANIPv4(models.Model):
	vlan = models.ForeignKey(VLANDescription, on_delete=models.CASCADE)
	ipv4net = models.ForeignKey(IPv4Network, on_delete=models.CASCADE)	

class VLANIPv6(models.Model):
	vlan = models.ForeignKey(VLANDescription, on_delete=models.CASCADE)
	ipv6address = models.ForeignKey(IPv6Network, on_delete=models.CASCADE)

class PortAllowedVLAN(models.Model):
	port = models.ForeignKey(Port, on_delete=models.CASCADE)
	vlan = models.ForeignKey(VLANIPv4, on_delete=models.CASCADE)
	native = models.BooleanField()

class PortCompat(models.Model):
	port1 = models.ForeignKey(PortInnerInterface, on_delete=models.CASCADE, related_name='compat_port1')
	port2 = models.ForeignKey(PortInnerInterface, on_delete=models.CASCADE, related_name='compat_port2')

class PortInterfaceCompat(models.Model):
	portinnerinterface = models.ForeignKey(PortInnerInterface, on_delete=models.CASCADE)
	portouterinterface = models.ForeignKey(PortOuterInterface, on_delete=models.CASCADE) 
	

class PortLog(models.Model):
	oldid = models.IntegerField()
	port = models.ForeignKey(Port, on_delete=models.CASCADE)
	date = models.DateTimeField()
	user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
	comment = models.TextField()

class PortVLANMode(models.Model):
	port = models.ForeignKey(Port, on_delete=models.CASCADE)
	trunk = models.BooleanField()

class RackObject(models.Model):
	oldid = models.IntegerField()
	name = models.TextField(255)
	label = models.TextField(255)
	objecttype = models.ForeignKey(ObjectType, on_delete=models.CASCADE)
	assetno = models.TextField(64)
	linkedobject = models.ForeignKey(Object, on_delete=models.SET_NULL, blank=True, null=True)
	hasproblems= models.BooleanField()
	comment = models.TextField()

class RackSpace(models.Model):
	rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
	unitno = models.IntegerField()
	atom = models.ForeignKey(Atom, on_delete=models.CASCADE)
	state = models.BooleanField()
	parentobject = models.ForeignKey(Object, on_delete=models.SET_NULL, blank=True, null=True)

class RackThumbnail(models.Model):
	rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
	data = models.BinaryField(102400)	

class Script(models.Model):
	name = models.TextField(64)
	content = models.TextField()

class Tag(models.Model):
	oldid = models.IntegerField()
	parenttag = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
	assignable = models.BooleanField()
	name = models.TextField()
	colour = models.BinaryField(3)
	description = models.TextField()

class TagFile(models.Model):
	file = models.ForeignKey(File, on_delete=models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
	date = models.DateTimeField()

class TagIPv4Network(models.Model):
	ipv4net = models.ForeignKey(IPv4Network, on_delete=models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
	date = models.DateTimeField()

class TagIPv4RSPool(models.Model):
	ipv4rspool = models.ForeignKey(IPv4RSPool, on_delete=models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
	date = models.DateTimeField()

class TagIPv4VS(models.Model):
	ipv4vs = models.ForeignKey(IPv4VS, on_delete=models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
	date = models.DateTimeField()

class TagIPv6Network(models.Model):
	ipv6network = models.ForeignKey(IPv6Network, on_delete=models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
	date = models.DateTimeField()

class TagLocation(models.Model):
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
	date = models.DateTimeField()

class TagObject(models.Model):
	object = models.ForeignKey(Object, on_delete=models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
	date = models.DateTimeField()

class TagRack(models.Model):
	rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
	user = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)
	date = models.DateTimeField()

class VLANSTRule(models.Model):
	oldid = models.IntegerField()
	rulenumber = models.IntegerField()
	portpcre = models.TextField(255)
	portrole = models.IntegerField(choices=choices.PortRole.choices)
	vlans = models.TextField(255)
	description = models.TextField(255)

class VLANSwitchTemplate(models.Model):
	oldid = models.IntegerField()
	revision = models.IntegerField()
	description = models.TextField(255)
	modifiedby = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, blank=True, null=True)	

class VLANSwitch(models.Model):
	parentobject = models.ForeignKey(Object, on_delete=models.CASCADE)
	domain = models.ForeignKey(VLANDomain, on_delete=models.CASCADE)
	template = models.ForeignKey(VLANSwitchTemplate, on_delete=models.SET_NULL, blank=True, null=True)
	revision = models.IntegerField()
	lasterror = models.IntegerField()
	lasterroroccured = models.DateTimeField()
	changed = models.DateTimeField()
	pushstarted = models.DateTimeField()
	pushended = models.DateTimeField()

class VLANValidID(models.Model):
	vlanid = models.SmallIntegerField()

class VS(models.Model):
	oldid = models.IntegerField()
	name = models.TextField(255)
	vsconfig = models.TextField()
	rsconfig = models.TextField()

class VSEnabledIPs(models.Model):
	parentobject = models.ForeignKey(Object, on_delete=models.CASCADE)
	parentvs = models.ForeignKey(VS, on_delete=models.CASCADE)
	rspool = models.ForeignKey(IPv4RSPool, on_delete=models.CASCADE)
	vip = models.ForeignKey(IPv4Address, on_delete=models.CASCADE)

class VSEnabledPorts(models.Model):
	parentobject = models.ForeignKey(Object, on_delete=models.CASCADE)
	parentvs = models.ForeignKey(VS, on_delete=models.CASCADE)
	protocol = bitflags.BitFlagField(choices=choices.Protocol)
	rspool = models.ForeignKey(IPv4RSPool, on_delete=models.CASCADE)
	port = models.ForeignKey(Port, on_delete=models.CASCADE)

class VSIPs(models.Model):
	parentvs = models.ForeignKey(VS, on_delete=models.CASCADE)
	ipv4address	= models.ForeignKey(IPv4Address, on_delete=models.CASCADE)

class VSPorts(models.Model):
	parentvs = models.ForeignKey(VS, on_delete=models.CASCADE)
	protocol = bitflags.BitFlagField(choices=choices.Protocol)
	port = models.SmallIntegerField()