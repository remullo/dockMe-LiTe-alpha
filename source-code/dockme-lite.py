import os
import sys
from os import listdir
from os.path import isfile, join


###licensing
	# 			Apache License
   #                         Version 2.0, January 2004
   #                      http://www.apache.org/licenses/
   #
   # TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
   #
   # 1. Definitions.
   #
   #    "License" shall mean the terms and conditions for use, reproduction,
   #    and distribution as defined by Sections 1 through 9 of this document.
   #
   #    "Licensor" shall mean the copyright owner or entity authorized by
   #    the copyright owner that is granting the License.
   #
   #    "Legal Entity" shall mean the union of the acting entity and all
   #    other entities that control, are controlled by, or are under common
   #    control with that entity. For the purposes of this definition,
   #    "control" means (i) the power, direct or indirect, to cause the
   #    direction or management of such entity, whether by contract or
   #    otherwise, or (ii) ownership of fifty percent (50%) or more of the
   #    outstanding shares, or (iii) beneficial ownership of such entity.
   #
   #    "You" (or "Your") shall mean an individual or Legal Entity
   #    exercising permissions granted by this License.
   #
   #    "Source" form shall mean the preferred form for making modifications,
   #    including but not limited to software source code, documentation
   #    source, and configuration files.
   #
   #    "Object" form shall mean any form resulting from mechanical
   #    transformation or translation of a Source form, including but
   #    not limited to compiled object code, generated documentation,
   #    and conversions to other media types.
   #
   #    "Work" shall mean the work of authorship, whether in Source or
   #    Object form, made available under the License, as indicated by a
   #    copyright notice that is included in or attached to the work
   #    (an example is provided in the Appendix below).
   #
   #    "Derivative Works" shall mean any work, whether in Source or Object
   #    form, that is based on (or derived from) the Work and for which the
   #    editorial revisions, annotations, elaborations, or other modifications
   #    represent, as a whole, an original work of authorship. For the purposes
   #    of this License, Derivative Works shall not include works that remain
   #    separable from, or merely link (or bind by name) to the interfaces of,
   #    the Work and Derivative Works thereof.
   #
   #    "Contribution" shall mean any work of authorship, including
   #    the original version of the Work and any modifications or additions
   #    to that Work or Derivative Works thereof, that is intentionally
   #    submitted to Licensor for inclusion in the Work by the copyright owner
   #    or by an individual or Legal Entity authorized to submit on behalf of
   #    the copyright owner. For the purposes of this definition, "submitted"
   #    means any form of electronic, verbal, or written communication sent
   #    to the Licensor or its representatives, including but not limited to
   #    communication on electronic mailing lists, source code control systems,
   #    and issue tracking systems that are managed by, or on behalf of, the
   #    Licensor for the purpose of discussing and improving the Work, but
   #    excluding communication that is conspicuously marked or otherwise
   #    designated in writing by the copyright owner as "Not a Contribution."
   #
   #    "Contributor" shall mean Licensor and any individual or Legal Entity
   #    on behalf of whom a Contribution has been received by Licensor and
   #    subsequently incorporated within the Work.
   #
   # 2. Grant of Copyright License. Subject to the terms and conditions of
   #    this License, each Contributor hereby grants to You a perpetual,
   #    worldwide, non-exclusive, no-charge, royalty-free, irrevocable
   #    copyright license to reproduce, prepare Derivative Works of,
   #    publicly display, publicly perform, sublicense, and distribute the
   #    Work and such Derivative Works in Source or Object form.
   #
   # 3. Grant of Patent License. Subject to the terms and conditions of
   #    this License, each Contributor hereby grants to You a perpetual,
   #    worldwide, non-exclusive, no-charge, royalty-free, irrevocable
   #    (except as stated in this section) patent license to make, have made,
   #    use, offer to sell, sell, import, and otherwise transfer the Work,
   #    where such license applies only to those patent claims licensable
   #    by such Contributor that are necessarily infringed by their
   #    Contribution(s) alone or by combination of their Contribution(s)
   #    with the Work to which such Contribution(s) was submitted. If You
   #    institute patent litigation against any entity (including a
   #    cross-claim or counterclaim in a lawsuit) alleging that the Work
   #    or a Contribution incorporated within the Work constitutes direct
   #    or contributory patent infringement, then any patent licenses
   #    granted to You under this License for that Work shall terminate
   #    as of the date such litigation is filed.
   #
   # 4. Redistribution. You may reproduce and distribute copies of the
   #    Work or Derivative Works thereof in any medium, with or without
   #    modifications, and in Source or Object form, provided that You
   #    meet the following conditions:
   #
   #    (a) You must give any other recipients of the Work or
   #        Derivative Works a copy of this License; and
   #
   #    (b) You must cause any modified files to carry prominent notices
   #        stating that You changed the files; and
   #
   #    (c) You must retain, in the Source form of any Derivative Works
   #        that You distribute, all copyright, patent, trademark, and
   #        attribution notices from the Source form of the Work,
   #        excluding those notices that do not pertain to any part of
   #        the Derivative Works; and
   #
   #    (d) If the Work includes a "NOTICE" text file as part of its
   #        distribution, then any Derivative Works that You distribute must
   #        include a readable copy of the attribution notices contained
   #        within such NOTICE file, excluding those notices that do not
   #        pertain to any part of the Derivative Works, in at least one
   #        of the following places: within a NOTICE text file distributed
   #        as part of the Derivative Works; within the Source form or
   #        documentation, if provided along with the Derivative Works; or,
   #        within a display generated by the Derivative Works, if and
   #        wherever such third-party notices normally appear. The contents
   #        of the NOTICE file are for informational purposes only and
   #        do not modify the License. You may add Your own attribution
   #        notices within Derivative Works that You distribute, alongside
   #        or as an addendum to the NOTICE text from the Work, provided
   #        that such additional attribution notices cannot be construed
   #        as modifying the License.
   #
   #    You may add Your own copyright statement to Your modifications and
   #    may provide additional or different license terms and conditions
   #    for use, reproduction, or distribution of Your modifications, or
   #    for any such Derivative Works as a whole, provided Your use,
   #    reproduction, and distribution of the Work otherwise complies with
   #    the conditions stated in this License.
   #
   # 5. Submission of Contributions. Unless You explicitly state otherwise,
   #    any Contribution intentionally submitted for inclusion in the Work
   #    by You to the Licensor shall be under the terms and conditions of
   #    this License, without any additional terms or conditions.
   #    Notwithstanding the above, nothing herein shall supersede or modify
   #    the terms of any separate license agreement you may have executed
   #    with Licensor regarding such Contributions.
   #
   # 6. Trademarks. This License does not grant permission to use the trade
   #    names, trademarks, service marks, or product names of the Licensor,
   #    except as required for reasonable and customary use in describing the
   #    origin of the Work and reproducing the content of the NOTICE file.
   #
   # 7. Disclaimer of Warranty. Unless required by applicable law or
   #    agreed to in writing, Licensor provides the Work (and each
   #    Contributor provides its Contributions) on an "AS IS" BASIS,
   #    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
   #    implied, including, without limitation, any warranties or conditions
   #    of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
   #    PARTICULAR PURPOSE. You are solely responsible for determining the
   #    appropriateness of using or redistributing the Work and assume any
   #    risks associated with Your exercise of permissions under this License.
   #
   # 8. Limitation of Liability. In no event and under no legal theory,
   #    whether in tort (including negligence), contract, or otherwise,
   #    unless required by applicable law (such as deliberate and grossly
   #    negligent acts) or agreed to in writing, shall any Contributor be
   #    liable to You for damages, including any direct, indirect, special,
   #    incidental, or consequential damages of any character arising as a
   #    result of this License or out of the use or inability to use the
   #    Work (including but not limited to damages for loss of goodwill,
   #    work stoppage, computer failure or malfunction, or any and all
   #    other commercial damages or losses), even if such Contributor
   #    has been advised of the possibility of such damages.
   #
   # 9. Accepting Warranty or Additional Liability. While redistributing
   #    the Work or Derivative Works thereof, You may choose to offer,
   #    and charge a fee for, acceptance of support, warranty, indemnity,
   #    or other liability obligations and/or rights consistent with this
   #    License. However, in accepting such obligations, You may act only
   #    on Your own behalf and on Your sole responsibility, not on behalf
   #    of any other Contributor, and only if You agree to indemnify,
   #    defend, and hold each Contributor harmless for any liability
   #    incurred by, or claims asserted against, such Contributor by reason
   #    of your accepting any such warranty or additional liability.
   #
   # END OF TERMS AND CONDITIONS
   #
   # Copyright (c) 2021 The dockME Project - Rêmullo B. G. M. Costa
   #
   # Licensed under the Apache License, Version 2.0 (the "License");
   # you may not use this file except in compliance with the License.
   # You may obtain a copy of the License at
   #
   #     http://www.apache.org/licenses/LICENSE-2.0
   #
   # Unless required by applicable law or agreed to in writing, software
   # distributed under the License is distributed on an "AS IS" BASIS,
   # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   # See the License for the specific language governing permissions and
   # limitations under the License.


##SOFTWARE
# Importar o módulo OS para poder utilizar este programa no terminal juntamente com o Autodock Vina
# Este software foi desenvolvido para tornar-se uma ferramenta facilitadora em pesquisa e desenvolvimento
# envolvendo bioinformática, biotecnologia e descoberta de novas drogas, viabilizando uma massiva quantidade de interações
# juntamente com o AutoDock Vina (NOTA: Certifique-se que 'vina.exe' esteja no diretório de trabalho e que esteja com este nome)


__author__ = "Rêmullo Costa,  Maria Aparecida,Amália Rêgo and Humberto Xavier-Júnior,"
__copyright__ = "Copyright 2021, The dockME-LITE's Project"
__credits__ = ["Rêmullo Costa"]
__license__ = "Apache"
__version__ = "1.0"
__maintainer__ = "Rêmullo Costa"
__email__ = "remullocosta@gmail.com"
__status__ = "Production"

##########################      ORIENTAÇÃO DE ORGANIZAÇÃO DOS ARQUIVOS DE POSIÇÃO DE GRADE #####################################
#   Além de auxiliar na organização do mapeamento das macromoléculas-alvo e ligantes, o método abaixo descrito é necessário para que este software funcione
#   de maneira limpa e adequada, uma vez que foi através deste modelo de organização que o mesmo foi concebido
#
#                     _______________________________________________
#                     ##        TABELA DE PROTEÍNAS                ##
#                     _______________________________________________
#                     ##| ORDEM |NOME DA MACROMOLÉCULA-ALVO(PDB*) |##
#                     ##|  0     |       PRO1                     |##
#                     ##|  1     |       PRO2                     |##
#                     ##|  2     |       PRO3                     |##
#                     ##|  3     |       PRO4                     |##
#                     ##|  ...   |       PRO(...)                 |##
#                     ##| (K**)  |       PRO(K)                   |##
#                     -----------------------------------------------
#                     * 'PDB' se refere ao código da MACROMOLÉCULA-ALVO nos bancos de dados de proteína disponíveis (Protein Data Banks)
#                     ** 'K' refere-se ao k-ésimo número da lista, trata-se de um exemplo de um número de ordem muito alta
#
#                     _________________________________________
#                     ##        TABELA DE LIGANTES          ##
#                     _________________________________________
#                     ##|   ORDEM |   NOME DO LIGANTE      |##
#                     ##|    0    |          LIG1          |##
#                     ##|    1    |          LIG2          |##
#                     ##|    2    |          LIG3          |##
#                     ##|    3    |          LIG4          |##
#                     ##|   ...   |          LIG(...)      |##
#                     ##|   (N*)  |          LIG(N)        |##
#                     -----------------------------------------
#                     * 'N' refere-se ao n-ésimo número da lista, trata-se de um exemplo de um número de ordem muito alta

# -------------NOTA: ---------------------------------------------------------------------------------------------------------------------------------------------#
# os arquivos de texto contendo as instruções de posição de grade (grid position) deverão ser nomeados conforme o exemplo a seguir:
# se o meu arquivo, por exemplo, tratar de uma interação da macromolécula "PRO2" com o ligante "LIG4", o arquivo que contemplar as informações de Grid que serão
# enviadas para o AutoDock Vina deverá ser escrito da seguinte forma: "1_3.txt" , ou seja, uma sequência de números que envolve as respectivas ordens de
# "PRO2" e "LIG4" separados por "_". ***********ATENÇÃO! O SOFTWARE NÃO FUNCIONARÁ ADEQUADAMENTE SE NÃO FOR ORGANIZADO DESTA FORMA!
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------#


#######LISTA DE LIGANTES UTILIZADOS
# Aqui, trata-se de uma lista que permitirá a este software nomear corretamente os arquivos de saída, portanto, sua ordem deverá respeitar a ordem da lista de ligantes
# previamente apresentada acima ["nome do item de ordem 0", "nome do item de ordem 1",...,"nome do item de ordem N"]

#o codigo abaixo permite nomear os ligantes
#liglist = ["NOME-DO-LIGANTE-1", "NOME-DO-LIGANTE-2", "NOME-DO-LIGANTE-(...)", "NOME-DO-LIGANTE-N"]
liglist = os.listdir('ligands')
########## FUTURAMENTE, PRETENDO IMPLEMENTAR OS LIGANTES RETIRANDO-OS DIRETAMENTE DO DIRETÓRIO DO USUÁRIO, ATRAVÉS DA FUNÇÃO:
# arquivos_ligands = os.listdir('ligands')

#######LISTA DE PROTEÍNAS UTILIZADAS
# Aqui, trata-se de uma lista que permitirá a este software nomear corretamente os arquivos de saída, portanto, sua ordem deverá respeitar a ordem da lista de PROTEÍNAS
#
# previamente apresentada acima ["nome do item de ordem 0", "nome do item de ordem 1", "nome do ítem de ordem (...)", "nome do item de ordem K"]


#O código abaixo permite ao usuário nomear
# protlist = ["NOME-OU-CÓDIGO-PDB-1", "NOME-OU-CÓDIGO-PDB-2", "NOME-OU-CODIGO-PDB-(...)", "NOME-OU-CÓDIGO-PDB-K"]
protlist = os.listdir('macromolecules')




########## FUTURAMENTE, PRETENDO IMPLEMENTAR AS PROTEINAS RETIRANDO-OS DIRETAMENTE DO DIRETÓRIO DO USUÁRIO, ATRAVÉS DA FUNÇÃO:
# dir_prot = os.listdir('protein')
# for i in range (0,len(dir_prot)):
#     if dir_prot(i).find('.pdbqt', 0):
#         dir_prot_list = dir_prot(i)
#
# print(dir_prot_list)
# ##criar uma lista com o nome dos arquivos de proteinas


########################################################### FUNÇÕES DESTE SOFTWARE ###########################################################################

##--------------------------------------ITERAÇÃO DAS K PROTEÍNAS COM OS N LIGANTES (OPTION 3)--------------------------------------------------------------------------------
def full_interact(k, n):
    if len(protlist) == 0 or len(liglist) <= 0:
        print('Nao ha arquivos nas pastas de macromoleculas ou ligantes!')
        main_menu()
    for k in range(0, len(protlist)):

        for n in range(0, len(liglist)):

            #os.system(" \"vina.exe\" --config %d" % (k) + "_" + "%d" % (n) + ".txt --log logfiles\%s" % protlist[k] + "_" + liglist[n] + "_log.txt")
            os.system(" \"vina.exe\" --config %d" % int(protlist[k].split(".",1)[0]) + "_" + "%d" % int(liglist[n].split(".",1)[0]) + ".txt --log logfiles\%s" % protlist[k].split(".",1)[0] + "_" + liglist[n].split(".",1)[0] + "_log.txt")

##----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


##----------------------------------INTERAÇÃO INDIVIDUAL ENTRE UMA MACROMOLÉCULA E UM LIGANTE---------------------------------------------------------------------
def single_interact():
    ##SOLICITA A ENTRADA DA ORDEM DA MACROMOLÉCULA DESEJADA
    solved = False
    if len(protlist) == 0 or len(liglist)<= 0:
        print('Nao ha arquivos nas pastas de macromoleculas ou ligantes!')
        main_menu()
    while not solved:
        print('lista de macromoleculas ', protlist)
        macro_order = int(input('Digite a ordem da macromolécula, com base na lista acima: ')) -1
        print('lista de ligantes ', liglist)
        lig_order = int(input('Digite a ordem do ligante, com base na lista acima: ')) -1


        if macro_order > len(protlist) or macro_order < 0 or lig_order > len(liglist) or lig_order < 0:
            quit_question = int(input('Ordem de macromolécula inválida! Deseja voltar ao menu principal? (y/n)'))
            proceder_prot = "y" or "Y"

            if quit_question == proceder_prot:
                main_menu()
                break

            else:
                solved_prot = False
        os.system(" \"vina.exe\" --config %d" % int(protlist[macro_order].split(".",1)[0]) + "_" + "%d" % int(liglist[lig_order].split(".",1)[0]) + ".txt --log logfiles\%s" % protlist[macro_order].split(".",1)[0] + "_" + liglist[lig_order].split(".",1)[0] + "_log.txt")
        main_menu()
        break


##------------------------------------------------------------------------------------------------------------------------------------------------------------

def main_menu():
    choice1 = False
    print("""NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNXK00KNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNK00KXNNNNNNNNNNNNXKKKKXNNNNNNXXKKKXNNNNNNNNNNNNNNNNNNNN
NNNNNNNNN0c;:dXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXd;;c0WNNNNNNNNNNxc::::o0NNNN0l::::ckNNNNNNNNNNNNNNNNNNN
NNNNNNNNNO:,,dXNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXo,,:0WNNNNNNNNNXo,,:c;;xXNNXo,;c:,,dXNNNNNNNNNNNNNNNNNN
NNKkdddxkx:,,dXNNNKkxddddxOKNNNNNKkxddddxk0NXo,,:0WNNKkxxkKNKl,,ox:,c0NNO:,cxl,,oXNNNXOxxdddxk0XNNNN
NOc,,;ccc:;,,dXNXx:,,:cc:,;:kXNXk:;,,::::ckNXo,,:0WN0l;,ckXNKl,,o0o,;xNXd,;d0l,,lKNNOl;,:clc;,;oKNNN
Kl,,:kXXXk:,,dXNk;,;o0XX0l,,:ONO:,,ckKKKKKXNXo,,:x0x:,;oKNNN0c,,oXO:,cK0c,c0Xo,,lKWKl,,cOXXXd;,;kNNN
0c,,lKNNNO:,;dXNd,,;xNNNXd;,;xNk;,,dXNNNNNNNXo,,;::;,;oKNNNN0c,;dXXo,;xd;,dXXo,,c0WO:,,:looo:,,l0NNN
0c,,c0WNNO:,,oXNd;,;xNNNXd;,;xNk;,,oXNNNNNNNXo,,:kKk:,;oKNNNO:,;dNNk:,::,:ONXd;,c0W0c,,;oxxxxkOKNNNN
Xd;,;lxxdc;,,dXNOc,,cxOOd:,,c0W0l,,;oxkkkxONXo,,:0WNOc,;l0NNO:,;xNNXxllllkXNKd;,:OWXd;,;lxkkkkxOXNNN
NKd:;;;:lxd::dXNNOoc:;;;;:cd0NNN0dc:;;;;;:xXXd::l0NNN0o::lONOc:ckNNNNNNNXKXXOdl:ckK0koc:;;;;;::dKNNN
NNNK000KXNXKKXNNNNNX00O00KXNNNNNNNXK00000KXNNXKKKXNNNNXKKKKNXKKKXNNNX0KXKO0KOkxkOOkOOkkkxxOO00KXNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKOk0KK00OkkO0OkkOOOOkOKXNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNXOk00Ok00kk0K0kkOOOOO0XNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN0kO0OkO0OkO0OkOOO00KXNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKkO0OkkOOkkOO0KXXNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKOkOOkkOO0KXXXNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNX0kkkO0KXXNNNNNNNNNNNNNNNNNNNNN""")
    print("Developed by Rêmullo B.G.M. Costa. ALl rights reserved.")
    print(" For more information, please check the full licensing statement at license.txt file")
    print(" ")
    print("Bem-vindo ao dockME!")
    while not choice1:
        
        print('Qual tarefa deseja realizar?')
        print('''
                    MENU:

                    [1] - Iniciar Interação COMPLETA entre Macromoleculas e ligantes
                    [2] - Iniciar Interação INDIVIDUAL entre Macromoleculas e ligantes
                    [3] - Sair
            ''')
        option_switch = int(input('Escolha uma opção: '))
        # while option_switch < 1 or option_switch > 4:
        #     option_switch = int(input('Ordem de ligante inválida! Escolha uma opção entre 1 e 4'))

        if option_switch == 1:
            full_interact(len(protlist), len(liglist))

        elif option_switch == 2:
            single_interact()

        elif option_switch == 3:
            print('Finalizado com êxito!')
            sys.exit()
        else:
            print('Entrada inválida! O sistema foi finalizado com êxito!')
            sys.exit()


# ------------------------------------------------------------------------------------------------------------------------



#-----------------------------------------
#main_window()



########################------------------------INÍCIO DO ALGORITMO-------------------------############################



# chamar o menu principal
main_menu()
