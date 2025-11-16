"""
OCSF MCP Server - Provides tools for interacting with the OCSF schema API

Requirements:
- pip install requests

This MCP server provides comprehensive access to the OCSF (Open Cybersecurity Schema Framework) API.
"""

from mcp.server.fastmcp import FastMCP
import requests
from typing import Optional, List, Dict, Any


mcp_server = FastMCP("OCSF MCP Server")

# OCSF API base URL
OCSF_BASE_URL = "https://schema.ocsf.io"


@mcp_server.tool()
def get_ocsf_schema() -> Dict[str, Any]:
    """Retrieve the OCSF schema as a string.

    Returns:
        str: The OCSF schema in string format.
    """
    try:
        response = requests.get(f"{OCSF_BASE_URL}/doc/swagger.json")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch schema: {str(e)}"}


@mcp_server.tool()
def get_ocsf_version() -> Dict[str, Any]:
    """Get the current OCSF schema version.

    Returns:
        Dict containing version information
    """
    try:
        response = requests.get(f"{OCSF_BASE_URL}/api/version")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch version: {str(e)}"}


@mcp_server.tool()
def get_ocsf_versions() -> Dict[str, Any]:
    """Get all available OCSF schema versions.

    Returns:
        Dict containing all available versions
    """
    try:
        response = requests.get(f"{OCSF_BASE_URL}/api/versions")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch versions: {str(e)}"}


@mcp_server.tool()
def get_ocsf_categories(extensions: Optional[List[str]] = None) -> Dict[str, Any]:
    """Get OCSF schema categories.

    Args:
        extensions: Optional list of extension names to include

    Returns:
        Dict containing category information
    """
    try:
        params = {}
        if extensions:
            params['extensions'] = extensions

        response = requests.get(
            f"{OCSF_BASE_URL}/api/categories", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch categories: {str(e)}"}


@mcp_server.tool()
def get_ocsf_category(name: str, extensions: Optional[List[str]] = None) -> Dict[str, Any]:
    """Get OCSF schema classes for a specific category.

    Args:
        name: Category name (may include extension, e.g., "dev/policy")
        extensions: Optional list of extension names to include

    Returns:
        Dict containing category classes
    """
    try:
        params = {}
        if extensions:
            params['extensions'] = extensions

        response = requests.get(
            f"{OCSF_BASE_URL}/api/categories/{name}", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch category '{name}': {str(e)}"}


@mcp_server.tool()
def get_ocsf_classes(extensions: Optional[List[str]] = None, profiles: Optional[List[str]] = None) -> Dict[str, Any]:
    """Get all OCSF schema classes.

    Args:
        extensions: Optional list of extension names to include
        profiles: Optional list of profile names to include

    Returns:
        Dict containing all classes
    """
    try:
        params = {}
        if extensions:
            params['extensions'] = extensions
        if profiles:
            params['profiles'] = profiles

        response = requests.get(f"{OCSF_BASE_URL}/api/classes", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch classes: {str(e)}"}


@mcp_server.tool()
def get_ocsf_class(name: str, profiles: Optional[List[str]] = None) -> Dict[str, Any]:
    """Get a specific OCSF schema class by name.

    Args:
        name: Class name (may include extension, e.g., "dev/cpu_usage")
        profiles: Optional list of profile names to include

    Returns:
        Dict containing class definition
    """
    try:
        params = {}
        if profiles:
            params['profiles'] = profiles

        response = requests.get(
            f"{OCSF_BASE_URL}/api/classes/{name}", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch class '{name}': {str(e)}"}


@mcp_server.tool()
def get_ocsf_objects(extensions: Optional[List[str]] = None) -> Dict[str, Any]:
    """Get all OCSF schema objects.

    Args:
        extensions: Optional list of extension names to include

    Returns:
        Dict containing all objects
    """
    try:
        params = {}
        if extensions:
            params['extensions'] = extensions

        response = requests.get(f"{OCSF_BASE_URL}/api/objects", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch objects: {str(e)}"}


@mcp_server.tool()
def get_ocsf_object(
    name: str,
    extensions: Optional[List[str]] = None,
    profiles: Optional[List[str]] = None
) -> Dict[str, Any]:
    """Get a specific OCSF schema object by name.

    Args:
        name: Object name (may include extension, e.g., "dev/os_service")
        extensions: Optional list of extension names to include
        profiles: Optional list of profile names to include

    Returns:
        Dict containing object definition
    """
    try:
        params = {}
        if extensions:
            params['extensions'] = extensions
        if profiles:
            params['profiles'] = profiles

        response = requests.get(
            f"{OCSF_BASE_URL}/api/objects/{name}", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch object '{name}': {str(e)}"}


@mcp_server.tool()
def get_ocsf_data_types() -> Dict[str, Any]:
    """Get OCSF schema data types.

    Returns:
        Dict containing data type definitions
    """
    try:
        response = requests.get(f"{OCSF_BASE_URL}/api/data_types")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch data types: {str(e)}"}


@mcp_server.tool()
def get_ocsf_dictionary(extensions: Optional[List[str]] = None) -> Dict[str, Any]:
    """Get OCSF schema dictionary.

    Args:
        extensions: Optional list of extension names to include

    Returns:
        Dict containing dictionary definitions
    """
    try:
        params = {}
        if extensions:
            params['extensions'] = extensions

        response = requests.get(
            f"{OCSF_BASE_URL}/api/dictionary", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch dictionary: {str(e)}"}


@mcp_server.tool()
def get_ocsf_profiles() -> Dict[str, Any]:
    """Get all OCSF schema profiles.

    Returns:
        Dict containing all profiles
    """
    try:
        response = requests.get(f"{OCSF_BASE_URL}/api/profiles")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch profiles: {str(e)}"}


@mcp_server.tool()
def get_ocsf_profile(name: str) -> Dict[str, Any]:
    """Get a specific OCSF schema profile by name.

    Args:
        name: Profile name (may include extension, e.g., "linux/linux_users")

    Returns:
        Dict containing profile definition
    """
    try:
        response = requests.get(f"{OCSF_BASE_URL}/api/profiles/{name}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch profile '{name}': {str(e)}"}


@mcp_server.tool()
def get_ocsf_extensions() -> Dict[str, Any]:
    """Get all OCSF schema extensions.

    Returns:
        Dict containing all extensions
    """
    try:
        response = requests.get(f"{OCSF_BASE_URL}/api/extensions")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch extensions: {str(e)}"}


@mcp_server.tool()
def validate_ocsf_event(event_data: Dict[str, Any], missing_recommended: bool = False) -> Dict[str, Any]:
    """Validate an OCSF event against the schema.

    Args:
        event_data: The event data to validate
        missing_recommended: Whether to warn about missing recommended attributes

    Returns:
        Dict containing validation results
    """
    try:
        params = {}
        if missing_recommended:
            params['missing_recommended'] = 'true'

        response = requests.post(
            f"{OCSF_BASE_URL}/api/v2/validate",
            json=event_data,
            params=params,
            headers={'Content-Type': 'application/json'}
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to validate event: {str(e)}"}


@mcp_server.tool()
def validate_ocsf_event_bundle(bundle_data: Dict[str, Any], missing_recommended: bool = False) -> Dict[str, Any]:
    """Validate an OCSF event bundle against the schema.

    Args:
        bundle_data: The event bundle data to validate
        missing_recommended: Whether to warn about missing recommended attributes

    Returns:
        Dict containing validation results for the bundle
    """
    try:
        params = {}
        if missing_recommended:
            params['missing_recommended'] = 'true'

        response = requests.post(
            f"{OCSF_BASE_URL}/api/v2/validate_bundle",
            json=bundle_data,
            params=params,
            headers={'Content-Type': 'application/json'}
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to validate event bundle: {str(e)}"}


@mcp_server.tool()
def translate_ocsf_event(event_data: Dict[str, Any], mode: int = 1, spaces: Optional[str] = None) -> Dict[str, Any]:
    """Translate OCSF event data using the schema.

    Args:
        event_data: The event data to translate
        mode: Translation mode (1=enum values, 2=enum+names, 3=verbose)
        spaces: How to handle spaces in translated names (empty string removes, other replaces)

    Returns:
        Dict containing translated event data
    """
    try:
        params: Dict[str, Any] = {'_mode': mode}
        if spaces is not None:
            params['_spaces'] = spaces

        response = requests.post(
            f"{OCSF_BASE_URL}/api/translate",
            json=event_data,
            params=params,
            headers={'Content-Type': 'application/json'}
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to translate event: {str(e)}"}


@mcp_server.tool()
def enrich_ocsf_event(event_data: Dict[str, Any], enum_text: bool = False, observables: bool = False) -> Dict[str, Any]:
    """Enrich OCSF event data with type_uid, enumerated text, and observables.

    Args:
        event_data: The event data to enrich
        enum_text: Whether to add enumerated text values
        observables: Whether to add observables array

    Returns:
        Dict containing enriched event data
    """
    try:
        params = {}
        if enum_text:
            params['_enum_text'] = 'true'
        if observables:
            params['_observables'] = 'true'

        response = requests.post(
            f"{OCSF_BASE_URL}/api/enrich",
            json=event_data,
            params=params,
            headers={'Content-Type': 'application/json'}
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to enrich event: {str(e)}"}


@mcp_server.tool()
def get_ocsf_sample_class(name: str, profiles: Optional[List[str]] = None) -> Dict[str, Any]:
    """Get sample data for a specific OCSF event class.

    Args:
        name: Class name (may include extension, e.g., "dev/cpu_usage")
        profiles: Optional list of profile names to include

    Returns:
        Dict containing sample event data
    """
    try:
        params = {}
        if profiles:
            params['profiles'] = profiles

        response = requests.get(
            f"{OCSF_BASE_URL}/sample/classes/{name}", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch sample for class '{name}': {str(e)}"}


@mcp_server.tool()
def get_ocsf_sample_object(name: str, profiles: Optional[List[str]] = None) -> Dict[str, Any]:
    """Get sample data for a specific OCSF object.

    Args:
        name: Object name (may include extension, e.g., "dev/os_service")
        profiles: Optional list of profile names to include

    Returns:
        Dict containing sample object data
    """
    try:
        params = {}
        if profiles:
            params['profiles'] = profiles

        response = requests.get(
            f"{OCSF_BASE_URL}/sample/objects/{name}", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch sample for object '{name}': {str(e)}"}


@mcp_server.tool()
def get_ocsf_base_event(profiles: Optional[List[str]] = None) -> Dict[str, Any]:
    """Get the OCSF base event class definition.

    Args:
        profiles: Optional list of profile names to include

    Returns:
        Dict containing base event definition
    """
    try:
        params = {}
        if profiles:
            params['profiles'] = profiles

        response = requests.get(
            f"{OCSF_BASE_URL}/api/base_event", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to fetch base event: {str(e)}"}


@mcp_server.tool()
def export_ocsf_schema(extensions: Optional[List[str]] = None, profiles: Optional[List[str]] = None) -> Dict[str, Any]:
    """Export the complete OCSF schema including data types, objects, classes, and dictionary.

    Args:
        extensions: Optional list of extension names to include
        profiles: Optional list of profile names to include

    Returns:
        Dict containing complete schema export
    """
    try:
        params = {}
        if extensions:
            params['extensions'] = extensions
        if profiles:
            params['profiles'] = profiles

        response = requests.get(
            f"{OCSF_BASE_URL}/export/schema", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": f"Failed to export schema: {str(e)}"}


if __name__ == "__main__":
    mcp_server.run(transport="stdio")
