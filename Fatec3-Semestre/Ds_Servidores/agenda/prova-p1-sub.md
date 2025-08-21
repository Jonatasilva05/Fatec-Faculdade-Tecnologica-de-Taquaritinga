

---

Opção 1:
```
function getById($conn, $id)
{
    $data = json_decode(file_get_contents('php://input'), true);
    (isset($data[ "id"])){
        try {
            $stmt = $conn->prepare("SELECT * FROM pessoas WHERE id = :id ");
            $stmt->bindParam(':id', $id);
            $stmt->execute();
            $pessoas = $stmt->fetchAll(PDO::FETCH_ASSOC);
            header('Content-Type: application/json');
            echo json_encode($pessoas);
        } catch (PDOException $e) {
            echo json_encode(['error' => $e->getMessage()]);
        }
    } else {
        echo json_encode(['error' => 'O id é obrigatório']);
    }
}
```
