// ============================================
// 1. Criar Banco de Dados (use db_name)
// ============================================

use empresa;  // Se o banco "empresa" não existir, será criado automaticamente ao inserir algo

// ============================================
// 2. Criar Coleção e Inserir Documentos
// ============================================

// Inserir um documento em uma nova coleção "clientes"
db.clientes.insertOne({
  nome: "Ana",
  idade: 30,
  cidade: "SP"
});

// Inserir vários documentos
db.clientes.insertMany([
  { nome: "Bruno", idade: 25, cidade: "RJ" },
  { nome: "Carlos", idade: 35, cidade: "SP" }
]);

// ============================================
// 3. Buscar Dados
// ============================================

// Buscar todos os documentos
db.clientes.find();

// Buscar clientes de SP
db.clientes.find({ cidade: "SP" });

// Buscar clientes com idade maior que 30
db.clientes.find({ idade: { $gt: 30 } });

// Buscar clientes ordenados por idade decrescente
db.clientes.find().sort({ idade: -1 });

// Buscar apenas nome e cidade (projeção)
db.clientes.find({}, { nome: 1, cidade: 1, _id: 0 });

// ============================================
// 4. Atualizar Dados
// ============================================

// Atualizar a idade de "Ana" para 32
db.clientes.updateOne(
  { nome: "Ana" },
  { $set: { idade: 32 } }
);

// Atualizar todas as idades adicionando +1
db.clientes.updateMany(
  {},
  { $inc: { idade: 1 } }
);

// ============================================
// 5. Excluir Dados
// ============================================

// Remover o cliente "Carlos"
db.clientes.deleteOne({ nome: "Carlos" });

// Remover todos os clientes de "RJ"
db.clientes.deleteMany({ cidade: "RJ" });

// ============================================
// 6. Contar Registros
// ============================================

// Contar todos os clientes
db.clientes.countDocuments();

// Contar clientes da cidade "SP"
db.clientes.countDocuments({ cidade: "SP" });

// ============================================
// 7. Criar Índices
// ============================================

// Criar índice no campo nome
db.clientes.createIndex({ nome: 1 });

// Criar índice composto: cidade + idade
db.clientes.createIndex({ cidade: 1, idade: -1 });
