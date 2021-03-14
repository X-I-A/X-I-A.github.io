import os
import json

seeder_schema = {
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
                                "format": "grid-strict",
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

pusher_schema = {
    "items": {
                        # "$ref": "https://repo.x-i-a.com/services/gcr/pusher.json?cache=0",
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
                                        "template": "pyagent",
                                        "options": {
                                            "grid_columns": 4,
                                        }
                                    },
                                    "_module": {
                                        "type": "string",
                                        "title": "Module Name",
                                        "template": "pyagent",
                                        "options": {
                                            "grid_columns": 4,
                                        }
                                    },
                                    "_class": {
                                        "type": "string",
                                        "title": "Class Name",
                                        "template": "Pusher",
                                        "options": {
                                            "grid_columns": 4,
                                            "grid_break": True,
                                        },
                                    },
                                    "adaptor": {
                                        "type": "string",
                                        "title": "Adaptor",
                                        "watch": {
                                            "adaptor": "modules",
                                        },
                                        "enumSource": [{
                                            "source": "adaptor",
                                            "filter": "{% if item.option._tags.includes('xialib.Adaptor') %}1{% endif %}",
                                            "value": "{{item.name}}"
                                        }],
                                        "options": {
                                            "grid_columns": 4,
                                        },
                                    },
                                },
                                "required": ["adaptor", "_package", "_module", "_class"],
                            },
                            "deploy": {
                                "type": "object",
                                "title": "Deployment options",
                                "format": "grid-strict",
                                "options": {
                                    "grid_columns": 12,
                                    "grid_break": True,
                                },
                                "properties": {
                                    "sa-name": {
                                        "type": "string",
                                        "title": "Service Account Name",
                                        "options": {
                                            "grid_columns": 4,
                                        }
                                    },
                                    "topics": {
                                        "type": "array",
                                        "title": "Connected Topics",
                                        "format": "table",
                                        "options": {
                                            "grid_columns": 8,
                                        },
                                        "minItems": 1,
                                        "uniqueItems": True,
                                        "items": {
                                            "type": "string",
                                            "title": "Connected Topics",
                                            "watch": {
                                                "seeder": "services.seeders",
                                                "dispatcher": "services.dispatcher.deploy.targets"
                                            },
                                            "enumSource": [{
                                                "source": "seeder",
                                                "value": "{{item.deploy.topic}}"
                                            },{
                                                "source": "dispatcher",
                                                "value": "{{item.topic}}"
                                            }],
                                        },
                                    },
                                },
                                "required": ["sa-name", "topics"],
                            }
                        },
                        "required": ["name", "service", "deploy"],
                    },
}

dispatcher_schema = {
    "dispatcher": {
                    # "$ref": "https://repo.x-i-a.com/services/gcr/dispatcher.json?cache=0",
                    "type": "object",
                    "title": "Dispatcher Service",
                    "format": "grid-strict",
                    "properties": {
                        "name": {
                            "type": "string",
                            "title": "Service Name",
                            "options": {
                                "grid_columns": 4,
                                "grid_break": True,
                            },
                            "default": "xia-dispatcher"
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
                                    "template": "Dispatcher",
                                    "options": {
                                        "grid_columns": 4,
                                        "grid_break": True,
                                    },
                                },
                                "publisher": {
                                    "type": "array",
                                    "title": "Publisher List",
                                    "format": "table",
                                    "uniqueItems": True,
                                    "items": {
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
                                    },
                                    "default": ["pubsub"],
                                },
                                "route_file": {
                                    "type": "string",
                                    "title": "Table specific routes file location",
                                    "options": {
                                        "grid_columns": 4,
                                    },
                                    "default": "config/routes.zip",
                                },
                                "storer": {
                                    "type": "string",
                                    "title": "Storer",
                                    "description": "Table specific routes file reader",
                                    "watch": {
                                        "storer": "modules"
                                    },
                                    "enumSource": [{
                                        "source": "storer",
                                        "filter": "{% if item.option._tags.includes('xialib.IOStorer') %}1{% endif %}",
                                        "value": "{{item.name}}"
                                    }],
                                    "options": {
                                        "grid_columns": 4,
                                        "grid_break": True,
                                    },
                                },
                            },
                            "required": ["publisher", "route_file", "_package", "_module", "_class"],
                        },
                        "deploy": {
                            "type": "object",
                            "title": "Deployment options",
                            "format": "grid-strict",
                            "options": {
                                "grid_columns": 12,
                                "grid_break": True,
                            },
                            "properties": {
                                "sa-name": {
                                    "type": "string",
                                    "title": "Service Account Name",
                                    "options": {
                                        "grid_columns": 4,
                                    }
                                },
                                "targets": {
                                    "type": "array",
                                    "format": "table",
                                    "title": "Target Topics",
                                    "uniqueItems": True,
                                    "items": {
                                        "type": "object",
                                        "title": "Target List",
                                        "properties": {
                                            "publisher_id": {
                                                "type": "string",
                                                "title": "Publisher",
                                                "watch": {
                                                    "publisher": "services.dispatcher.service.publisher",
                                                },
                                                "enumSource": [{
                                                    "source": "publisher",
                                                }],
                                                "options": {
                                                    "grid_columns": 4,
                                                },
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
                                        },
                                        "required": ["publisher_id", "destination", "topic"],
                                    },
                                },
                                "sources": {
                                    "type": "array",
                                    "title": "Source Topics",
                                    "format": "table",
                                    "options": {
                                        "grid_columns": 12,
                                    },
                                    "minItems": 1,
                                    "uniqueItems": True,
                                    "items": {
                                        "type": "string",
                                        "title": "Source Topics",
                                        "watch": {
                                            "seeder": "services.seeders"
                                        },
                                        "enumSource": [{
                                            "source": "seeder",
                                            "value": "{{item.deploy.topic}}"
                                        }],
                                    },
                                },
                                "routes": {
                                    "type": "array",
                                    "title": "Topic Level Routes",
                                    "format": "table",
                                    "description": "Apply when no table level routes found",
                                    "options": {
                                        "grid_columns": 12,
                                    },
                                    "uniqueItems": True,
                                    "items": {
                                        "type": "object",
                                        "title": "Target List",
                                        "properties": {
                                            "source": {
                                                "type": "string",
                                                "title": "Source",
                                                "watch": {
                                                    "source": "services.dispatcher.deploy.sources",
                                                },
                                                "enumSource": [{
                                                    "source": "source",
                                                }],
                                                "options": {
                                                    "grid_columns": 6,
                                                },
                                            },
                                            "target": {
                                                "type": "string",
                                                "title": "Target",
                                                "watch": {
                                                    "target": "services.dispatcher.deploy.targets",
                                                },
                                                "enumSource": [{
                                                    "source": "target",
                                                    "value": "{{item.topic}}"
                                                }],
                                                "options": {
                                                    "grid_columns": 6,
                                                },
                                            },
                                        },
                                        "required": ["source", "target"],
                                    },
                                }
                            },
                            "required": ["sa-name"],
                        }
                    },
                    "required": ["name", "service", "deploy"],
                },
}

data_lake_schema = {
    "data-lake": {
                    # "$ref": "https://repo.x-i-a.com/services/gcr/data-lake.json?cache=0",
                    "type": "object",
                    "title": "Data Lake",
                    "format": "grid-strict",
                    "properties": {
                        "in": {
                            "type": "string",
                            "title": "Data Receive Endpoint",
                            "options": {
                                "grid_columns": 4,
                            },
                        },
                        "out": {
                            "type": "string",
                            "title": "Data Load Endpoint",
                            "options": {
                                "grid_columns": 4,
                                "grid_break": True,
                            },
                        },
                        "name-prefix": {
                            "type": "string",
                            "title": "Service Name Prefix",
                            "options": {
                                "grid_columns": 4,
                            },
                            "default": "xia-",
                        },
                        "sa-prefix": {
                            "type": "string",
                            "title": "Service Account Name Prefix",
                            "options": {
                                "grid_columns": 4,
                                "grid_break": True,
                            },
                            "default": "gcr-xia-",
                        },
                        "depositor": {
                            "type": "string",
                            "title": "Depositor",
                            "options": {
                                "grid_columns": 4,
                            },
                            "watch": {
                                "depositor": "modules",
                            },
                            "enumSource": [{
                                "source": "depositor",
                                "filter": "{% if item.option._tags.includes('xialib.Depositor') %}1{% endif %}",
                                "value": "{{item.name}}"
                            }],
                        },
                        "archiver": {
                            "type": "string",
                            "title": "Archiver",
                            "options": {
                                "grid_columns": 4,
                            },
                            "watch": {
                                "archiver": "modules",
                            },
                            "enumSource": [{
                                "source": "archiver",
                                "filter": "{% if item.option._tags.includes('xialib.Archiver') %}1{% endif %}",
                                "value": "{{item.name}}"
                            }],
                        },
                        "services": {
                            "type": "object",
                            "title": "Data Lake Sub-Services",
                            "format": "categories",
                            "options": {
                                "grid_columns": 12,
                            },
                            "properties": {
                                "loader": {
                                    "type": "object",
                                    "title": "Loader",
                                    "format": "grid-strict",
                                    "properties": {
                                        "name": {
                                            "type": "string",
                                            "title": "Service Name",
                                            "options": {
                                                "grid_columns": 4,
                                                "grid_break": True,
                                            },
                                            "template": "{{prefix}}loader",
                                            "watch": {
                                                "prefix": "services.data-lake.name-prefix",
                                            },
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
                                                    "template": "Loader",
                                                    "options": {
                                                        "grid_columns": 4,
                                                        "grid_break": True,
                                                    },
                                                },
                                                "depositor": {
                                                    "type": "string",
                                                    "title": "Depositor",
                                                    "options": {
                                                        "grid_columns": 4,
                                                    },
                                                    "template": "{{depositor}}",
                                                    "watch": {
                                                        "depositor": "services.data-lake.depositor",
                                                    },
                                                },
                                                "archiver": {
                                                    "type": "string",
                                                    "title": "Archiver",
                                                    "options": {
                                                        "grid_columns": 4,
                                                        "grid_break": True,
                                                    },
                                                    "template": "{{archiver}}",
                                                    "watch": {
                                                        "archiver": "services.data-lake.archiver",
                                                    },
                                                },
                                                "publisher": {
                                                    "type": "array",
                                                    "title": "Publisher Dictionary",
                                                    "format": "table",
                                                    "uniqueItems": True,
                                                    "options": {
                                                        "grid_columns": 4,
                                                    },
                                                    "items": {
                                                        "type": "string",
                                                        "title": "publisher",
                                                        "watch": {
                                                            "publisher": "modules",
                                                        },
                                                        "enumSource": [{
                                                            "source": "publisher",
                                                            "filter": "{% if item.option._tags.includes('xialib.Publisher') %}1{% endif %}",
                                                            "value": "{{item.name}}"
                                                        }],
                                                    },
                                                    "default": ['pubsub'],
                                                },
                                                "storer": {
                                                    "type": "string",
                                                    "title": "Storer",
                                                    "description": "Table specific routes file reader",
                                                    "options": {
                                                        "grid_columns": 4,
                                                    },
                                                    "template": "{{storer}}",
                                                    "watch": {
                                                        "storer": "services.dispatcher.service.storer",
                                                    },
                                                },
                                                "route_file": {
                                                    "type": "string",
                                                    "title": "Table specific routes file location",
                                                    "options": {
                                                        "grid_columns": 4,
                                                        "grid_break": True,
                                                    },
                                                    "template": "{{route_file}}",
                                                    "watch": {
                                                        "route_file": "services.dispatcher.service.route_file",
                                                    },
                                                },
                                            },
                                            "required": ["_package", "_module", "_class", "depositor", "archiver",
                                                         "route_file", "publisher"],
                                        },
                                        "deploy": {
                                            "type": "object",
                                            "title": "Deployment options",
                                            "format": "grid-strict",
                                            "options": {
                                                "grid_columns": 12,
                                                "grid_break": True,
                                            },
                                            "properties": {
                                                "sa-name": {
                                                    "type": "string",
                                                    "title": "Service Account Name",
                                                    "options": {
                                                        "grid_columns": 4,
                                                        "grid_break": True,
                                                    },
                                                    "template": "{{prefix}}loader",
                                                    "watch": {
                                                        "prefix": "services.data-lake.sa-prefix",
                                                    },
                                                },
                                            },
                                            "required": ["sa-name"],
                                        }
                                    },
                                    "required": ["name", "service", "deploy"],
                                },
                                "cleaner": {
                                    "type": "object",
                                    "title": "Cleaner",
                                    "format": "grid-strict",
                                    "properties": {
                                        "name": {
                                            "type": "string",
                                            "title": "Service Name",
                                            "options": {
                                                "grid_columns": 4,
                                                "grid_break": True,
                                            },
                                            "template": "{{prefix}}cleaner",
                                            "watch": {
                                                "prefix": "services.data-lake.name-prefix",
                                            },
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
                                                    "template": "Cleaner",
                                                    "options": {
                                                        "grid_columns": 4,
                                                        "grid_break": True,
                                                    },
                                                },
                                                "depositor": {
                                                    "type": "string",
                                                    "title": "Depositor",
                                                    "options": {
                                                        "grid_columns": 4,
                                                    },
                                                    "template": "{{depositor}}",
                                                    "watch": {
                                                        "depositor": "services.data-lake.depositor",
                                                    },
                                                },
                                                "archiver": {
                                                    "type": "string",
                                                    "title": "Archiver",
                                                    "options": {
                                                        "grid_columns": 4,
                                                        "grid_break": True,
                                                    },
                                                    "template": "{{archiver}}",
                                                    "watch": {
                                                        "archiver": "services.data-lake.archiver",
                                                    },
                                                },
                                            },
                                            "required": ["_package", "_module", "_class", "depositor", "archiver"],
                                        },
                                        "deploy": {
                                            "type": "object",
                                            "title": "Deployment options",
                                            "format": "grid-strict",
                                            "options": {
                                                "grid_columns": 12,
                                                "grid_break": True,
                                            },
                                            "properties": {
                                                "sa-name": {
                                                    "type": "string",
                                                    "title": "Service Account Name",
                                                    "options": {
                                                        "grid_columns": 4,
                                                        "grid_break": True,
                                                    },
                                                    "template": "{{prefix}}cleaner",
                                                    "watch": {
                                                        "prefix": "services.data-lake.sa-prefix",
                                                    },
                                                },
                                            },
                                            "required": ["sa-name"],
                                        }
                                    },
                                    "required": ["name", "service", "deploy"],
                                },
                                "merger": {
                                    "type": "object",
                                    "title": "Merger",
                                    "format": "grid-strict",
                                    "properties": {
                                        "name": {
                                            "type": "string",
                                            "title": "Service Name",
                                            "options": {
                                                "grid_columns": 4,
                                                "grid_break": True,
                                            },
                                            "template": "{{prefix}}merger",
                                            "watch": {
                                                "prefix": "services.data-lake.name-prefix",
                                            },
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
                                                    "template": "Merger",
                                                    "options": {
                                                        "grid_columns": 4,
                                                        "grid_break": True,
                                                    },
                                                },
                                                "depositor": {
                                                    "type": "string",
                                                    "title": "Depositor",
                                                    "options": {
                                                        "grid_columns": 4,
                                                        "grid_break": True,
                                                    },
                                                    "template": "{{depositor}}",
                                                    "watch": {
                                                        "depositor": "services.data-lake.depositor",
                                                    },
                                                },
                                            },
                                            "required": ["_package", "_module", "_class", "depositor"],
                                        },
                                        "deploy": {
                                            "type": "object",
                                            "title": "Deployment options",
                                            "format": "grid-strict",
                                            "options": {
                                                "grid_columns": 12,
                                                "grid_break": True,
                                            },
                                            "properties": {
                                                "sa-name": {
                                                    "type": "string",
                                                    "title": "Service Account Name",
                                                    "options": {
                                                        "grid_columns": 4,
                                                        "grid_break": True,
                                                    },
                                                    "template": "{{prefix}}merger",
                                                    "watch": {
                                                        "prefix": "services.data-lake.sa-prefix",
                                                    },
                                                },
                                            },
                                            "required": ["sa-name"],
                                        }
                                    },
                                    "required": ["name", "service", "deploy"],
                                },
                                "packager": {
                                    "type": "object",
                                    "title": "Packager",
                                    "format": "grid-strict",
                                    "properties": {
                                        "name": {
                                            "type": "string",
                                            "title": "Service Name",
                                            "options": {
                                                "grid_columns": 4,
                                                "grid_break": True,
                                            },
                                            "template": "{{prefix}}packager",
                                            "watch": {
                                                "prefix": "services.data-lake.name-prefix",
                                            },
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
                                                    "template": "Packager",
                                                    "options": {
                                                        "grid_columns": 4,
                                                        "grid_break": True,
                                                    },
                                                },
                                                "depositor": {
                                                    "type": "string",
                                                    "title": "Depositor",
                                                    "options": {
                                                        "grid_columns": 4,
                                                    },
                                                    "template": "{{depositor}}",
                                                    "watch": {
                                                        "depositor": "services.data-lake.depositor",
                                                    },
                                                },
                                                "archiver": {
                                                    "type": "string",
                                                    "title": "Archiver",
                                                    "options": {
                                                        "grid_columns": 4,
                                                        "grid_break": True,
                                                    },
                                                    "template": "{{archiver}}",
                                                    "watch": {
                                                        "archiver": "services.data-lake.archiver",
                                                    },
                                                },
                                            },
                                            "required": ["_package", "_module", "_class", "depositor", "archiver"],
                                        },
                                        "deploy": {
                                            "type": "object",
                                            "title": "Deployment options",
                                            "format": "grid-strict",
                                            "options": {
                                                "grid_columns": 12,
                                                "grid_break": True,
                                            },
                                            "properties": {
                                                "sa-name": {
                                                    "type": "string",
                                                    "title": "Service Account Name",
                                                    "options": {
                                                        "grid_columns": 4,
                                                        "grid_break": True,
                                                    },
                                                    "template": "{{prefix}}packager",
                                                    "watch": {
                                                        "prefix": "services.data-lake.sa-prefix",
                                                    },
                                                },
                                            },
                                            "required": ["sa-name"],
                                        }
                                    },
                                    "required": ["name", "service", "deploy"],
                                },
                                "receiver": {
                                    "type": "object",
                                    "title": "Receiver",
                                    "format": "grid-strict",
                                    "properties": {
                                        "name": {
                                            "type": "string",
                                            "title": "Service Name",
                                            "options": {
                                                "grid_columns": 4,
                                                "grid_break": True,
                                            },
                                            "template": "{{prefix}}receiver",
                                            "watch": {
                                                "prefix": "services.data-lake.name-prefix",
                                            },
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
                                                    "template": "Receiver",
                                                    "options": {
                                                        "grid_columns": 4,
                                                        "grid_break": True,
                                                    },
                                                },
                                                "depositor": {
                                                    "type": "string",
                                                    "title": "Depositor",
                                                    "options": {
                                                        "grid_columns": 4,
                                                        "grid_break": True,
                                                    },
                                                    "template": "{{depositor}}",
                                                    "watch": {
                                                        "depositor": "services.data-lake.depositor",
                                                    },
                                                },
                                            },
                                            "required": ["_package", "_module", "_class", "depositor"],
                                        },
                                        "deploy": {
                                            "type": "object",
                                            "title": "Deployment options",
                                            "format": "grid-strict",
                                            "options": {
                                                "grid_columns": 12,
                                                "grid_break": True,
                                            },
                                            "properties": {
                                                "sa-name": {
                                                    "type": "string",
                                                    "title": "Service Account Name",
                                                    "options": {
                                                        "grid_columns": 4,
                                                        "grid_break": True,
                                                    },
                                                    "template": "{{prefix}}receiver",
                                                    "watch": {
                                                        "prefix": "services.data-lake.sa-prefix",
                                                    },
                                                },
                                            },
                                            "required": ["sa-name"],
                                        }
                                    },
                                    "required": ["name", "service", "deploy"],
                                },
                            },
                            "required": ["cleaner", "merger", "receiver", "packager", "loader"],
                        },
                    },
                    "required": ["name-prefix", "sa-prefix", "depositor", "archiver", "services"],
                },
}

with open(os.path.join('..', 'services', 'gcr', 'seeder.json'), 'w') as fp:
    fp.write(json.dumps(seeder_schema["items"], ensure_ascii=False, indent=2))

with open(os.path.join('..', 'services', 'gcr', 'pusher.json'), 'w') as fp:
    fp.write(json.dumps(pusher_schema["items"], ensure_ascii=False, indent=2))

with open(os.path.join('..', 'services', 'gcr', 'dispatcher.json'), 'w') as fp:
    fp.write(json.dumps(dispatcher_schema["dispatcher"], ensure_ascii=False, indent=2))

with open(os.path.join('..', 'services', 'gcr', 'data-lake.json'), 'w') as fp:
    fp.write(json.dumps(data_lake_schema["data-lake"], ensure_ascii=False, indent=2))