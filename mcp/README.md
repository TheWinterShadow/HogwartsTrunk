# OCSF MCP Server

A Model Context Protocol (MCP) server providing comprehensive access to the OCSF (Open Cybersecurity Schema Framework) API.

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the server:
   ```bash
   python coding.py
   ```

## Features

### Schema Information Tools
- `get_ocsf_version()` - Get current OCSF schema version
- `get_ocsf_versions()` - Get all available schema versions
- `get_ocsf_extensions()` - Get all available extensions
- `get_ocsf_profiles()` - Get all available profiles
- `get_ocsf_profile(name)` - Get specific profile details

### Categories and Classes
- `get_ocsf_categories([extensions])` - Get all event categories
- `get_ocsf_category(name, [extensions])` - Get classes in specific category
- `get_ocsf_classes([extensions], [profiles])` - Get all event classes
- `get_ocsf_class(name, [profiles])` - Get specific class definition
- `get_ocsf_base_event([profiles])` - Get base event class

### Objects and Data Types
- `get_ocsf_objects([extensions])` - Get all schema objects
- `get_ocsf_object(name, [extensions], [profiles])` - Get specific object definition
- `get_ocsf_data_types()` - Get all data type definitions
- `get_ocsf_dictionary([extensions])` - Get schema dictionary

### Event Processing Tools
- `validate_ocsf_event(event_data, [missing_recommended])` - Validate single event
- `validate_ocsf_event_bundle(bundle_data, [missing_recommended])` - Validate event bundle
- `translate_ocsf_event(event_data, [mode], [spaces])` - Translate event using schema
- `enrich_ocsf_event(event_data, [enum_text], [observables])` - Enrich event with metadata

### Sample Data
- `get_ocsf_sample_class(name, [profiles])` - Get sample data for event class
- `get_ocsf_sample_object(name, [profiles])` - Get sample data for object

### Schema Export
- `export_ocsf_schema([extensions], [profiles])` - Export complete schema

### File-based Schema
- `get_ocsf_schema()` - Get schema from local file (legacy function)

## Usage Examples

### Get all event categories
```python
categories = get_ocsf_categories()
```

### Validate an event
```python
event = {
    "class_uid": 1001,
    "activity_id": 1,
    "time": 1689125893360905
}
validation_result = validate_ocsf_event(event)
```

### Get sample data for a class
```python
sample = get_ocsf_sample_class("file_activity")
```

### Translate event with enumerated text
```python
translated = translate_ocsf_event(event, mode=2, spaces="_")
```

## API Reference

All functions return dictionaries containing the API response or error information. Optional parameters are wrapped in brackets.

For detailed API documentation, visit: https://schema.ocsf.io/doc/index.html