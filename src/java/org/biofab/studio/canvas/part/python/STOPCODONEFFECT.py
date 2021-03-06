'''
 ######################################################################### 
 #  Copyright (C) 2010 Dokyun Na <blisszen@kaist.ac.kr>                  #
 #                                                                       #
 #  This program is based on algorithms developed by researchers at      #
 #  KAIST: Korea Advanced Institute of Science and Technology, and       #
 #   published in the paper:                                             #
 #                                                                       #
 #    Mathematical modeling of translation initiation for the            #
 #    estimation of its efficiency to computationally design mRNA        #
 #    sequences with a desired expression level in prokaryotes.          #
 #                  BMC Systems Biology (2010) 4(1): 71                  #
 #                  http://www.biomedcentral.com/1752-0509/4/71          #
 #                                          -- Na et al.                 #
 #                                                                       #
 #  This program is free software; you can redistribute it and/or        #
 #  modify it under the terms of the GNU Affero General Public License   #
 #  as published by the Free Software Foundation; either version 3, or   #
 #  any later version.                                                   #
 #                                                                       #
 #  Commercial licensing of this program is also possible.               #
 #  Contact Dokyun Na <blisszen@kaist.ac.kr>                             #
 #        or Doheon Lee <dhlee@kaist.ac.kr> for information about        #
 #  commercial licensing options.                                        #
 #                                                                       #
 #  This program is distributed in the hope that it will be useful, but  #
 #  WITHOUT ANY WARRANTY; without even the implied warranty of           #
 #  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU    #
 #  General Public License for more details.                             #
 #                                                                       #
 #  You should have received a copy of the GNU Affero General Public     #
 #  License along with this program (in the COPYING.txt file) if not,    #
 #  write to the Free Software Foundation, Inc.,                         #
 #  51 Franklin St, Fifth Floor, Boston, MA                              #
 #  02110-1301, USA.                                                     #
 #                                                                       #
 #########################################################################
'''


def calculateStopCodonEffect(stopcodon):

    
    stopcodon = stopcodon.upper().replace('U','T')
    
    r = 1.0
    if stopcodon=='TAAT':
        r = 1.0
    elif stopcodon =='TAAG':
        r=0.625
    elif stopcodon =='TAAA':
        r=0.4375
    elif stopcodon=='TAAC':
        r=0.4375
    elif stopcodon =='TGAT':
        r=0.875
    elif stopcodon=='TGAG':
        r=0.625
    elif stopcodon=='TGAA':
        r=0.3125
    elif stopcodon=='TGAC':
        r= 0.125
    elif stopcodon=='TAGT':
        r=0.75
    elif stopcodon=='TAGG':
        r=0.875
    elif stopcodon=='TAGA':
        r=0.625
    elif stopcodon=='TAGC':
        r=0.25
    elif stopcodon=='':
        r = 1.0
    else:
        #r = 1.0
        print 'Unknown stop codon'
        sys.exit(1)
        
    return r
    
