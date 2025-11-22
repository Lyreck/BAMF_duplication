import json
# code from Claude.

def export_for_visualization(result, output_file='graph_data.json'):
    """
    Export Soundex results to JSON for the JavaScript visualization.
    
    Args:
        result: Output from find_duplicates_with_soundex
        output_file: Path to output JSON file
    """
    
    # Prepare nodes - include all duplicates and some isolated
    nodes = []
    
    for item in result['all_duplicates']: ## TO CHANGE WITH REAL DATA

        nodes.append({
            'name': item, # item['name'],
            'expected': None, # item['expected'],
            'id': None, # item['id'],
            'soundex': None, # item['soundex'],
            'has_duplicates': True
        })
    
    
    # Create Soundex group information
    soundex_info = {}
    for code, group in result['duplicate_groups'].items():
        soundex_info[code] = [item for item in group] #[item['name'] for item in group]
    
    output = {
        'nodes': nodes,
        'soundex_groups': soundex_info,
        'stats': result['stats']
    }
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"Data exported to {output_file}")
    print(f"\nStats:")
    print(f"  Total records: {result['stats']['total_records']}")
    print(f"  Soundex groups with duplicates: {result['stats']['duplicate_groups']}")
    print(f"  Potential duplicate names: {result['stats']['potential_duplicates']}")
    
    return output