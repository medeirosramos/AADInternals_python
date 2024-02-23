from AADInternals import AADInternals

#ONLY If multi-factor authentication NOT enable:
az = AADInternals(mail="user",password="senha")

#If multi-factor authentication enable:
az = AADInternals(tenant_id='id')

#enable sync password feature
#print(az.set_sync_features(enable_features=['PasswordHashSync']))
#AUTENTICACAO DE PASSAGEM
print(az.set_sync_features(enable_features=['PassThroughAuthentication']))


#create account
#az.set_azureadobject('sourceanchortest',"test@mydomain.com",netBiosName='MYDOMAIN',givenName='givenName',dnsDomainName='dnsDomainName',displayName="displayName",surname='surname',commonName='commonName')
# debora.bessa account test
az.set_azureadobject('501eeeb1-14ff-494f-8712-a3320d245ad2',"debora.bessa@norteng.com.br",netBiosName='AD',givenName='DEBORA',dnsDomainName='ad.norteng.com.br',displayName="DEBORA MONALISA JUSTO BESSA",surname='BESSA',commonName='DEBORA MONALISA JUSTO BESSA')


#Send password (if error is "2")  please wait ...
#print(az.set_userpassword(hashnt="8846F7EAEE8FB117AD06BDD830B7586C",sourceanchor='sourceanchortest'))

#create group with member
#print(az.set_azureadobject("testgroup",usertype='Group',SecurityEnabled=True,displayName='testgroup',groupMembers=["sourceanchortest"]))

