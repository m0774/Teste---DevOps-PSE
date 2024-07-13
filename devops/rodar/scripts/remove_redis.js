const fs = require('fs');
const path = require('path');

const diretorioRaiz = '../applications'; 

function removerConfigRedis(caminho) {
    fs.readFile(caminho, 'utf8', (err, data) => {
        if (err) {
            console.error(`Erro ao ler arquivo: ${err}`);
            return;
        }

        const regexRedis = /redisConfig|redis/g;
        const novoConteudo = data.replace(regexRedis, '');

        fs.writeFile(caminho, novoConteudo, 'utf8', (err) => {
            if (err) {
                console.error(`Erro ao escrever arquivo: ${err}`);
                return;
            }
            console.log(`Configurações redis removidas de: ${caminho}`);
        });
    });
}

function percorrerDiretorio(diretorio) {
    fs.readdir(diretorio, (err, arquivos) => {
        if (err) {
            console.error(`Erro ao ler diretório: ${err}`);
            return;
        }

        arquivos.forEach((arquivo) => {
            const caminhoCompleto = path.join(diretorio, arquivo);
            fs.stat(caminhoCompleto, (err, stat) => {
                if (err) {
                    console.error(`Erro ao verificar arquivo: ${err}`);
                    return;
                }
                if (stat.isFile()) {
                    removerConfigRedis(caminhoCompleto);
                } else if (stat.isDirectory()) {
                    percorrerDiretorio(caminhoCompleto);
                }
            });
        });
    });
}

percorrerDiretorio(diretorioRaiz);
