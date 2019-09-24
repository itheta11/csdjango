from mongoengine import Document, EmbeddedDocument, fields


class Projects(EmbeddedDocument):
    projectId = fields.StringField(max_length = 5, required= True, null= False)
    projectName = fields.StringField(max_length= 20, required= True, null= True)
    startDate = fields.DateTimeField()
    endDate = fields.DateTimeField()


class Skills(EmbeddedDocument):
    tech = fields.StringField(max_length= 20, required= True, null=False)
    experience = fields.StringField(max_length= 20,required= True, null=False)
    level = fields.StringField(max_length= 20, required=True, null= False)


class Employee(Document):
    empId = fields.StringField(max_length= 5, required= True, null= False)
    empName = fields.StringField(max_length= 20, required= True, null=False)
    workLocation = fields.StringField(max_length= 20, required= True, null=False)

    projects = fields.EmbeddedDocumentListField(Projects)
    skills = fields.EmbeddedDocumentListField(Skills)