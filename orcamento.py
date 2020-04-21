#programador: Diego Franco
#data: 20/10/2019

''' Este programa tem como objetivo facilitar o orçamento de sessoes fotográficas'''
import os

def validaEntrada(string):
    
    entrada = 0
    while entrada <= 0:
        try:
            entrada = float(input(string))
        except ValueError:
            pass
    return entrada


def recebeEntrada(string1, string2):

	inputString = '0'
	while inputString != 's' and inputString != 'n':
		inputString = (input(string1))
		if inputString == 's':
			custoString = validaEntrada(string2)
		elif inputString == 'n':
			custoString = 0
		else:
			print("entre com \'s\' para sim e \'n\' para não.")
	return custoString


def main():

	inputConfig = '0'
	while inputConfig != 's' and inputConfig != 'n':
		inputConfig = input("Usar as configurações de equipamento, investimento e despesas com ferramentas de edição salvas?(s/n) ")
		if inputConfig == 's':
			custoMaterial = 9700
			investimentoProfissional = 200
			outrasDespesas = 100
			custoMarketing = 0
		elif inputConfig == 'n':
			custoMaterial = validaEntrada("Qual o valor aproximado do seu equipamento?(Camêras, Lentes, Flashes, Tripés, etc): ")
			investimentoProfissional = validaEntrada("Quanto já investiu/investe em cursos e/ou workshops profissionalizantes? ")
			custoMarketing = recebeEntrada("Investe em marketing e/ou atração de clientes?(Anúncios pagos, Hospedagem de site, Impulsionamento em mídias socias): ", "Qual a sua despesa mensal com marketing? ")

	'''
	#temporariamente desabilitado por falta de uso.
	custoAluguel = recebeEntrada("Salão comercial?(s/n) ", "Qual o valor do aluguel? ")
		
	if custoAluguel > 0:
		despesasMensais = validaEntrada("E as despesas mensais do estabelecimento?(Água, Luz, Internet, Telefone): ")
	else:
		despesasMensais = 0

	custoFuncionarios = recebeEntrada("Possui funcionários?(s/n) ", "Qual a sua despesa mensal com funcionários? ")
	'''

	mediaTrabalhosMes = validaEntrada("Quantos trabalhos em média você prevê realizar esse mês? ")
	
	if mediaTrabalhosMes < 1:
		mediaTrabalhosMes = 1
	elif mediaTrabalhosMes > 10:
		mediaTrabalhosMes = 10

	horaTrabalho = validaEntrada("Qual o valor da sua hora de trabalho? ")
	nHoras = validaEntrada("Serão quantas horas de trabalho? ")
	nHoras *= 4

	custoDeslocamento = recebeEntrada("Terá custo de deslocamento para o local ou aluguel de estúdio?(s/n) ", "Qual a sua despesa total com deslocamento ou aluguel do estúdio? ")
	outrasDespesas = recebeEntrada("Possui alguma outra despesa não descrita acima?(s/n) ", "Qual o valor? ")

	orcamento = (custoMaterial/36) + (investimentoProfissional/mediaTrabalhosMes) + (custoMarketing/mediaTrabalhosMes) + (outrasDespesas/mediaTrabalhosMes)
	#orcamento = orcamento + (custoFuncionarios/mediaTrabalhosMes) + (custoAluguel/mediaTrabalhosMes) + (despesasMensais/mediaTrabalhosMes)
	orcamento = ((orcamento/20) + horaTrabalho)*nHoras + custoDeslocamento

	print("O valor sugerido para este trabaho é de R$:%.2f" % orcamento)
	os.system("PAUSE")
	
main()
