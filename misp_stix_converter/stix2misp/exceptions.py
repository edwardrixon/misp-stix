# -*- coding: utf-8 -*-
#!/usr/bin/env python3


class STIXtoMISPError(Exception):
    def __init__(self, message):
        super(STIXtoMISPError, self).__init__(message)
        self.message = message


class UndefinedSTIXObjectError(STIXtoMISPError):
    pass


class UnknownAttributeTypeError(STIXtoMISPError):
    pass


class UnknownObjectNameError(STIXtoMISPError):
    pass