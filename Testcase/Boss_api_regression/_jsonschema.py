import jsonschema
import unittest

class _Jsonschema_:
    u"""jsonchema validata try..."""

    @classmethod
    def __init__(self,TestName):
        self.TestName = TestName


    def jsonschema_PhysicalNode(self):

        PhysicalNode = {"type":"object",
                        "$schema": "http://json-schema.org/draft-03/schema",
                        "required": False,
                        "properties":{
                        "data":{"type":"array",
                                "required":True,
                                "properties":{
                                    "physical_node_id": {
                                        "type":"string",
                                        "required":True
                                    },
                                    "physical_node_name": {
                                    "type":"string",
                                    "required":False
                                    },
                                    "isp": {
                                        "type":"string",
                                        "required":True
                                     },
                                    "large_area": {
                                      "type":"string",
                                      "required":True
                                    },
                                    "node_level": {
                                      "type":"string",
                                      "required":True
                                    },
                                    "province": {
                                      "type":"string",
                                      "required":True
                                    },
                                    "min_limit": {
                                      "type":"number",
                                      "required":True
                                    },
                                    "max_limit": {
                                      "type":"number",
                                      "required":True
                                    },
                                    "is_delete11": {
                                      "type":"number",
                                      "required":True
                                    }
                      }
                    }
                            }}

        return PhysicalNode

        # try:
        #     temp = jsonschema.validate(data, schema)
        #
        #     print("jsonschema.validate Result:%s"%temp)
        #
        # except jsonschema.ValidationError as e:
        #     print(e.message)
        # except jsonschema.SchemaError as e:
        #     print(e)
        # print("jsonschema.Draft3Validator.validate..")
        #
        # try:
        #     temp = jsonschema.Draft3Validator(schema).validate(data)
        #     print("jsonschema.Draft3Validator.validate Result:%s"%temp)
        #
        # except jsonschema.ValidationError as e:
        #     print(e.message)

    # @classmethod
    # def tearDownClass(self):
    #     pass
#
# if __name__ == '__main__':
#
#     Jsonschema_temp(TestName= "PhysicalNode").jsonschema()