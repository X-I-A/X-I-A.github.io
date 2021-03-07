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
with open(os.path.join('..', 'services', 'gcr', 'seeder.json'), 'w') as fp:
    fp.write(json.dumps(seeder_schema["items"], ensure_ascii=False, indent=2))

with open(os.path.join('..', 'services', 'gcr', 'pusher.json'), 'w') as fp:
    fp.write(json.dumps(pusher_schema["items"], ensure_ascii=False, indent=2))

with open(os.path.join('..', 'services', 'gcr', 'dispatcher.json'), 'w') as fp:
    fp.write(json.dumps(dispatcher_schema["dispatcher"], ensure_ascii=False, indent=2))