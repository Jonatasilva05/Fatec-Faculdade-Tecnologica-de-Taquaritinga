using _20_03;

IPagamento polianaPagamento = new Cash(150, "Poliana");
polianaPagamento.processarPagamento();

IPagamento guilhermePagamento = new CartaoCredito(1000, "Guilherme");
guilhermePagamento.processarPagamento();

IPagamento japonesaPagamento = new CartaoDebito(200, "Japonesa");
japonesaPagamento.processarPagamento();

IPagamento andrePagamento = new Pix();
andrePagamento.processarPagamento();

IPagamento estornarMaiconPagamento = new CartaoCredito(100, "Maicon");
estornarMaiconPagamento.estornarPagamento();