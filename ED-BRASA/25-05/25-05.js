class No{
    constructor(valor){
        this.valor = valor;
        this.proximo = null;
    }
}

// CLasse Lista
class lista{
    constructor(){
        this.cabeca = null;
    }
    // Adiciona um No na lista
    adicina(valor){
        const novoNo = new No(valor);
        if(this.cabeca === null){
        this.cabeca = novoNo;
    } else {
        let atual = this.cabeca;
        while(atual.proximo !== null){
                atual = atual.proximo;
            }
            atual.proximo = novoNo;
        }
    }
    remover(valor){
    if(this.cabeca === null)
        return;
    if(this.cabeca.valor === valor){
        this.cabeca = this.cabeca.proximo;
        return;
    }
    let atual = this.cabeca;
    }
    imprimir(){
        let atual = this.cabeca;
        let resultado = '';
        while(atual !== null){
            resultado += atual.valor + '->';
            atual = atual.proximo;
        }
        document.write(resultado + 'null');
    }
}