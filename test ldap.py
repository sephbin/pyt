import ldap
con = ldap.initialize('ldap://localhost:389', bytes_mode=False)
con.simple_bind_s(u'login', u'secret_password')
results = con.search_s(u'ou=people,dc=example,dc=org', ldap.SCOPE_SUBTREE, u"(cn=Raphaël)")