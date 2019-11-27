from django import template

register = template.Library()

@register.simple_tag(name='prestador_servico')
def list_prestador_servico(tipo_prestador_servico):
    prestadores_servico = PrestadorServico.objects.filter(tipo_prestador_servico = tipo_prestador_servico).order_by('nome')
    return  prestadores_servico