from django.db import models
from django import forms
from django.utils.translation import gettext as _

class BitFlagFormField(forms.MultipleChoiceField):
    widget = forms.CheckboxSelectMultiple

    def __init__(self, *args, **kwargs):
        super(BitFlagFormField, self).__init__(*args, **kwargs)

class BitFlagField(models.PositiveBigIntegerField):
	
	description = _("Bit flags field, up to 64 bits")

	def __init__(self, *args, **kwargs):

		choices = kwargs['choices']

		self.choicesdict = {}

		#Creating a dict for lookups
		for value, label in choices:
			self.choicesdict[value] = label

		kwargs['choices'] = self.choicesdict.items()
		#kwargs['max_length'] = 8

		super().__init__(*args, **kwargs)

	def deconstruct(self):
		name, path, args, kwargs = super().deconstruct()

		#del kwargs['max_length']

		return name, path, args, kwargs

	def from_db_value(self, value, expression, connection):
		if value is None:
			return value
		return decode_choices(value)

	def to_python(self, value):
		return decode_choices(value)

	def get_prep_value(self, value):
		return encode_choices(value)

	def decode_choices(value):
		result = []
		bit_no = 1
		while value > 0:
			if (value % 2 > 0):
				result.append(choicesdict[bit_no])
			bit_no *= 2
			value /= 2

		return result

	def encode_choices(value):
		result = 0

		for choice in value:
			for key in choicesdict:
				if choice == choicesdict[key]:
					result += key

		return result