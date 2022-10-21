from django.db import models

class ValueType(models.IntegerChoices):
	STRING = 1
	UINT = 2
	FLOAT = 3
	DICT = 4
	DATE = 5

class AllocType(models.IntegerChoices):
	REGULAR = 1
	SHARED = 2
	VIRTUAL = 3
	ROUTER = 4
	POINT2POINT = 5
	SHAREDROUTER = 6

class VLANType(models.IntegerChoices):
	ONDEMAND = 1
	COMPULSORY = 2
	ALIEN = 3

class PortRole(models.IntegerChoices):
	ACCESS = 1
	TRUNK = 2
	ANYMODE = 3
	UPLINK = 4
	DOWNLINK = 5
	NONE = 6

Protocol = (
	(1,'TCP'),
	(2,'UDP'),
	(4,'ICMP'),
)

XAxis = (
	(1,'Left'),
	(2,'Center'),
	(4,'Right'),
)

YAxis = (
	(1,'Bottom'),
	(2,'Center'),
	(4,'Top'),
)

ZAxis = (
	(1,'Front'),
	(2,'Center'),
	(4,'Back'),
)