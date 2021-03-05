import json

service_schema = {
    "items": {
                        #"$ref": "https://repo.x-i-a.com/services/gcr/seeder.json?cache=0",
                        "type": "object",
                        "headerTemplate": "{{ self.name }}",
                        "format": "grid-strict",
                        "properties": {
                            "name": {
                                "type": "string",
                                "title": "Service Name",
                                "options": {
                                    "grid_columns": 4,
                                    "grid_break": True,
                                }
                            },
                            "service": {
                                "type": "object",
                                "title": "Service Configuration",
                                "format": "grid-strict",
                                "options": {
                                    "grid_columns": 12,
                                    "grid_break": True,
                                    "display_required_only": True,
                                },
                                "properties": {
                                    "_package": {
                                        "type": "string",
                                        "title": "Pypi Package Name",
                                        "template": "pyxeed",
                                        "options": {
                                            "grid_columns": 4,
                                        }
                                    },
                                    "_module": {
                                        "type": "string",
                                        "title": "Module Name",
                                        "template": "pyxeed",
                                        "options": {
                                            "grid_columns": 4,
                                        }
                                    },
                                    "_class": {
                                        "type": "string",
                                        "title": "Class Name",
                                        "template": "Seeder",
                                        "options": {
                                            "grid_columns": 4,
                                            "grid_break": True,
                                        },
                                    },
                                    "publisher": {
                                        "type": "string",
                                        "title": "Publisher",
                                        "watch": {
                                            "publisher": "modules",
                                        },
                                        "enumSource": [{
                                            "source": "publisher",
                                            "filter": "{% if item.option._tags.includes('xialib.Publisher') %}1{% endif %}",
                                            "value": "{{item.name}}"
                                        }],
                                        "options": {
                                            "grid_columns": 4,
                                        },
                                        "default": "pubsub",
                                    },
                                    "storer": {
                                        "type": "array",
                                        "title": "Storer List",
                                        "format": "table",
                                        "uniqueItems": True,
                                        "items": {
                                            "type": "string",
                                            "title": "storer",
                                            "watch": {
                                                "storer": "modules",
                                            },
                                            "enumSource": [{
                                                "source": "storer",
                                                "filter": "{% if item.option._tags.includes('xialib.Storer') %}1{% endif %}",
                                                "value": "{{item.name}}"
                                            }],
                                        },
                                    },
                                    "formatter": {
                                        "type": "array",
                                        "title": "Formatter List",
                                        "format": "table",
                                        "uniqueItems": True,
                                        "items": {
                                            "type": "string",
                                            "title": "formatter",
                                            "watch": {
                                                "storer": "modules",
                                            },
                                            "enumSource": [{
                                                "source": "formatter",
                                                "filter": "{% if item.option._tags.includes('xialib.Formatter') %}1{% endif %}",
                                                "value": "{{item.name}}"
                                            }],
                                        },
                                    },
                                    "decoder": {
                                        "type": "array",
                                        "title": "Decoder List",
                                        "format": "table",
                                        "uniqueItems": True,
                                        "items": {
                                            "type": "string",
                                            "title": "decoder",
                                            "watch": {
                                                "storer": "modules",
                                            },
                                            "enumSource": [{
                                                "source": "decoder",
                                                "filter": "{% if item.option._tags.includes('xialib.Decoder') %}1{% endif %}",
                                                "value": "{{item.name}}"
                                            }],
                                        },
                                    },
                                    "translator": {
                                        "type": "array",
                                        "title": "Translator List",
                                        "format": "table",
                                        "uniqueItems": True,
                                        "items": {
                                            "type": "string",
                                            "title": "translator",
                                            "watch": {
                                                "storer": "modules",
                                            },
                                            "enumSource": [{
                                                "source": "decoder",
                                                "filter": "{% if item.option._tags.includes('xialib.Translator') %}1{% endif %}",
                                                "value": "{{item.name}}"
                                            }],
                                        },
                                    },
                                },
                                "required": ["publisher", "_package", "_module", "_class"],
                            },
                            "deploy": {
                                "type": "object",
                                "title": "Deployment options",
                                "format": "grid",
                                "options": {
                                    "grid_columns": 12,
                                    "grid_break": True,
                                },
                                "properties": {
                                    "insight": {
                                        "type": "boolean",
                                        "title": "Save to Data Lake?",
                                        "options": {
                                            "grid_columns": 4,
                                        }
                                    },
                                    "destination": {
                                        "type": "string",
                                        "title": "Destination",
                                        "options": {
                                            "grid_columns": 4,
                                        }
                                    },
                                    "topic": {
                                        "type": "string",
                                        "title": "Topic ID",
                                        "options": {
                                            "grid_columns": 4,
                                            "grid_break": True,
                                        },
                                    },
                                    "sa-name": {
                                        "type": "string",
                                        "title": "Service Account Name",
                                        "options": {
                                            "grid_columns": 4,
                                        }
                                    },
                                },
                                "required": ["insight", "destination", "topic", "sa-name"],
                            }
                        },
                        "required": ["name", "service", "deploy"],
                    },
}

with open('seeder.json', 'w') as fp:
    fp.write(json.dumps(service_schema["items"], ensure_ascii=False, indent=2))