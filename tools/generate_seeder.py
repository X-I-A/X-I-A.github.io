import json

service_schema = {
                        "type": "object",
                        "headerTemplate": "{{ self._deploy.name }}",
                        "format": "grid-strict",
                        "properties": {
                            "_deploy": {
                                "type": "object",
                                "format": "grid-strict",
                                "options": {
                                    "grid_columns": 12,
                                    "grid_break": True,
                                },
                                "properties": {
                                    "name": {
                                        "type": "string",
                                        "title": "Service Name",
                                        "options": {
                                            "grid_columns": 4,
                                        }
                                    },
                                    "insight": {
                                        "type": "boolean",
                                        "title": "Save to Data Lake?",
                                        "options": {
                                            "grid_columns": 4,
                                        },
                                    },
                                }
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
                                    "grid_break": True,
                                },
                                "default": "pubsub",
                            },
                            "_package": {
                                "type": "string",
                                "title": "Pypi Package Name",
                                "template": "pyinsight",
                                "options": {
                                    "grid_columns": 4,
                                }
                            },
                            "_module": {
                                "type": "string",
                                "title": "Module Name",
                                "template": "pyinsight",
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
                        "required": ["name", "insight", "publisher", "_package", "_module", "_class"],
                        "options": {
                            "display_required_only": True,
                        },
                    },

with open('service.json', 'w') as fp:
    fp.write(json.dumps(service_schema, ensure_ascii=False, indent=2))