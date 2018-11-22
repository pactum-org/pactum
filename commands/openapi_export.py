import importlib
import json

import click
import yaml
from pactum.exporters.openapi import OpenAPIV3Exporter


def clean_dict(d):
    if not isinstance(d, (dict, list)):
        return d
    if isinstance(d, list):
        return [v for v in (clean_dict(v) for v in d) if v]
    return {k: v for k, v in ((k, clean_dict(v)) for k, v in d.items()) if v not in (None, '', [], {})}


@click.command()
@click.argument('spec_file', type=click.Path())
@click.argument('output_file', type=click.File(mode='w'))
@click.option('--format', type=click.Choice(['json', 'yaml']), default='json')
def openapi_export(spec_file, output_file, format):
    spec = importlib.machinery.SourceFileLoader('spec', spec_file).load_module()
    api = spec.api
    visitor = OpenAPIV3Exporter()
    api.accept(visitor)
    result = clean_dict(visitor.result)
    if format == 'json':
        json.dump(result, output_file, indent=2)
    elif format == 'yaml':
        yaml.dump(result, output_file, default_flow_style=False)
