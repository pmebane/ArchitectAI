def function_schema():
    function_schema = {
        "type": "object",
        "properties": {
            "recommendations": {
            "type": "array",
            "items": 
                {
                "type": "object",
                "properties": {
                    "tech": {"type": "string", "description": "the technology that was recommended by the assistant, e.g. Data Warehouse"},
                    "reasoning": {"type": "string", "description": "why the technology was recommended"},
                    "vendors": {
                    "type": "array",
                    "items": 
                        {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string", "description": "name of the vendor that was recommended"},
                            "reasoning": {"type": "string", "description": "why the vendor was recommended"}
                        },
                        "required": ["name","reasoning"]
                        }
                    
                    }
                },
                "required": ["tech","reasoning","vendors"]
                }
            
            }
        },
        "required": ["recommendations"]
        }
    return function_schema