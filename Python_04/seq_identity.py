#!/usr/bin/env python3
#insert the output from clustalW online server here in triple quotes

alignment = '''gi|170746|gb|M12277.1|WHTH4091      ------------------------------------------------------------	0
gi|603555|emb|X83548.1|             TCTAGAGATGGCGCCATTTGATTCCAGCAGCCACAAAGCACTAGAACAATCGATGCTAAG	60
gi|170746|gb|M12277.1|WHTH4091      -------------------------AGCACCCTCCCACCTCATCCCACCCTTCTGATCTC	35
gi|603555|emb|X83548.1|             AGGTGACAGGAAAAACAGGCTGCAAAGACCCAGACAATGGAATGCAGCGGTGGTCAGCCT	120
gi|170746|gb|M12277.1|WHTH4091      AATCCAACGTCGCATCTCCACCGTCTCGC-----GGATCGACCCAGCGAAGTCC----CT	86
gi|603555|emb|X83548.1|             AAAACACTGTAGAAGGGCAAGATGAGCTGAGTAATTTTTAACTGGGCATCATTTTTAGAA	180
gi|170746|gb|M12277.1|WHTH4091      CCCGCCCCCAAAGTCCC----------CCAAATCTTGCAGTTCCCTCCTAAATCCTCCCC	136
gi|603555|emb|X83548.1|             ACTGGAGTTTAAGTACCCCCTTTTCCATTTTTTCCTGAAGTCGTGGGCAGGGCGCAAGGT	240
gi|170746|gb|M12277.1|WHTH4091      ATATAAACCAACCCCCCGCCCTCAGATCCCTAATC-CCATCGCA--AGCATCAGACTCCC	193
gi|603555|emb|X83548.1|             CTGTGAATCGGCCGACCGGATGCAGCTGGTGTGGAGAGTTCCCAATCAGGTCCGATTTAT	300
gi|170746|gb|M12277.1|WHTH4091      TCCAAAGCAGGCAGCAGCTCCTCTTCTTCCTAATCACACTATCTCGGAGAGGAGCGGCCA	253
gi|603555|emb|X83548.1|             TACTATATAAAGTACTGCTGC--GAGGCTTGCCGTGTTGCATTTTGTTTAGTACAAGACA	358
gi|170746|gb|M12277.1|WHTH4091      TGTCTGGGCGCGACAAGGGCGGCAAGGGGCTGGGCAAGGGCGGCGCCAAGCGGCACCGGA	313
gi|603555|emb|X83548.1|             TGTCTGGGCGCGGCAAAGGCGGGAAGGGTCTGGGCAAAGGAGGCGCTAAGCGCCACCGCA	418
gi|170746|gb|M12277.1|WHTH4091      AGGTCCTCCGCGACAACATCCAGGGCATCACCAAGCCGGCGATCCGGAGGCTGGCCAGGA	373
gi|603555|emb|X83548.1|             AAGTTCTGCGCGACAACATTCAGGGCATCACCAAGCCCGCCATCCGACGCCTGGCACGGC	478
gi|170746|gb|M12277.1|WHTH4091      GGGGCGGCGTGAAGCGCATCTCCGGCCTCATCTACGAGGAGACCCGCGGCGTCCTCAAGA	433
gi|603555|emb|X83548.1|             GTGGAGGCGTTAAGCGCATCTCAGGCCTTATATACGAGGAGACACGCGGAGTTCTTAAAG	538
gi|170746|gb|M12277.1|WHTH4091      TCTTCCTCGAGAACGTCATCCGCGACGCCGTCACCTACACCGAGCACGCCCGCCGCAAAA	493
gi|603555|emb|X83548.1|             TGTTTTTGGAGAATGTAATCCGCGATGCAGTTACCTACACGGAGCACGCCAAACGCAAGA	598
gi|170746|gb|M12277.1|WHTH4091      CCGTCACCGCCATGGACGTCGTCTACGCGCTCAAGCGCCAGGGCCGCACCCTCTACGGCT	553
gi|603555|emb|X83548.1|             CAGTCACAGCCATGGACGTGGTTTACGCGCTCAAGCGCCAGGGCCGCACCCTGTATGGCT	658
gi|170746|gb|M12277.1|WHTH4091      TCGGAGGCTAGATTTGTGTGGTGAAGCAACTTCCTCGTTTGCTCTGTGATCTGTGCTGTC	613
gi|603555|emb|X83548.1|             TTGGCGGCTGAGTGTTTTACTTACTTACACGGTTCCTCAAAGGCCCTTCTCAGGGCCACC	718
gi|170746|gb|M12277.1|WHTH4091      GTAGATGAGATTTACTGATTTGGCGTGCGCC---GGTTGTATTCTGTCATGGGGTTCAGT	670
gi|603555|emb|X83548.1|             CATGAAGTCTGTGAAAGAGCTGTAGACTAAAGATAGTTAATTTCTTAAGAAC-----ACT	773
gi|170746|gb|M12277.1|WHTH4091      GGGCTGTGTAATACCTTGCTCTGTACTTCTGTTCAA----TGCAATCACTTCTATTC---	723
gi|603555|emb|X83548.1|             TAAACGTATGGCAGTTTTGGCAAATTAGCGATTCCACATAAGCAGTCGCTGAAGTTTGAG	833
gi|170746|gb|M12277.1|WHTH4091      ----------------TGAA-----------------	727
gi|603555|emb|X83548.1|             GTTCGGTGCCCCTTTCAGCATTACTTAGTGGTTAAAA	870'''

print(alignment)

alignment = alignment.split('\n')

if len(alignment) % 2 != 0: print('WARNING odd number of lines in the alignment')
else:
 global_identity = 0
 for i in range(int(len(alignment)/2)):
   line1 = alignment[i].split()[1]
   line2 = alignment[i+1].split()[1]
   identity = 1 - (line1.count('-') + line2.count('-')) / len(line1)
   global_identity += identity

   print(line1)
   print(line2)

 global_identity = global_identity * 2 / len(alignment)
 print(global_identity)




  












