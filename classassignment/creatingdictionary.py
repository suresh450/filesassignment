s="EDFFX2AD \dat_out_sig_reg[0]  ( .D(N69), .E(N96), .CK(clk), .Q(dat_out[0]));"
t=(s.split(' ',1))
tkey=t[0]
tvalue=t[1]
tdict={tkey:tvalue}
print(tdict)