# Imports
import sqlite3

# Queries
query1 = 'SELECT COUNT(character_id) \
          FROM charactercreator_character;'
query2a = 'SELECT COUNT(character_ptr_id) \
           FROM charactercreator_mage;'
query2b = 'SELECT COUNT(character_ptr_id) \
           FROM charactercreator_thief;'
query2c = 'SELECT COUNT(character_ptr_id) \
           FROM charactercreator_cleric;'
query2d = 'SELECT COUNT(character_ptr_id) \
           FROM charactercreator_fighter;'
query2e = 'SELECT COUNT(mage_ptr_id) \
           FROM charactercreator_necromancer;'
query3 = 'SELECT COUNT(item_id) \
          FROM armory_item;'
query4a = 'SELECT COUNT(name) \
           FROM armory_item \
           INNER JOIN armory_weapon \
           ON armory_item.item_id = armory_weapon .item_ptr_id;'
query4b = 'SELECT COUNT(name) \
           FROM armory_item \
           WHERE item_id \
           NOT IN \
               (SELECT item_ptr_id \
                FROM armory_weapon);'
query5 = 'SELECT cc.name, COUNT(ai.name) \
          FROM charactercreator_character AS cc, \
               armory_item AS ai, \
               charactercreator_character_inventory AS cci \
          WHERE cc.character_id = cci.character_id \
            AND ai.item_id = cci.item_id \
          GROUP BY ai.name \
          ORDER BY COUNT(ai.name) DESC \
          LIMIT 20;'
query6 = 'SELECT cc.name, COUNT(ai.name) \
          FROM charactercreator_character AS cc, \
               armory_item AS ai, \
               charactercreator_character_inventory AS cci, \
               armory_weapon AS aw \
               WHERE cc.character_id = cci.character_id \
                 AND ai.item_id = cci.item_id \
                 AND ai.item_id = aw.item_ptr_id \
               GROUP BY ai.name \
               ORDER BY COUNT(ai.name) DESC \
               LIMIT 20;'
query7 = 'SELECT AVG(COUNT) \
          FROM \
              (SELECT COUNT(ai.name) AS COUNT \
               FROM charactercreator_character AS cc, \
                    armory_item AS ai, \
                    charactercreator_character_inventory AS cci \
               WHERE cc.character_id = cci.character_id \
                 AND ai.item_id = cci.item_id \
                 GROUP BY ai.name\
              ) ;'
query8 = 'SELECT AVG(COUNT) \
          FROM \
              (SELECT COUNT(ai.name) AS COUNT \
               FROM charactercreator_character AS cc, \
                    armory_item AS ai, \
                    charactercreator_character_inventory AS cci, \
                    armory_weapon AS aw \
                    WHERE cc.character_id = cci.character_id \
                      AND ai.item_id = cci.item_id \
                      AND ai.item_id = aw.item_ptr_id \
                      GROUP BY ai.name\
              );'


conn = sqlite3.connect('rpg_db.sqlite3')

# Execute queries
curs1 = conn.cursor()
print('Total characters =', curs1.execute(query1).fetchall())

curs2a = conn.cursor()
print('Total mage =', curs2a.execute(query2a).fetchall())

curs2b = conn.cursor()
print('Total thief =', curs2a.execute(query2b).fetchall())

curs2c = conn.cursor()
print('Total cleric =', curs2c.execute(query2c).fetchall())

curs2d = conn.cursor()
print('Total fighter =', curs2d.execute(query2d).fetchall())

curs2e = conn.cursor()
print('Total necromancer =', curs2e.execute(query2e).fetchall())

curs3 = conn.cursor()
print('Total items =', curs3.execute(query3).fetchall())

curs4a = conn.cursor()
print('Total items are weapons =', curs4a.execute(query4a).fetchall())

curs4b = conn.cursor()
print('Total items not weapons =', curs4b.execute(query4b).fetchall())

curs5 = conn.cursor()
print('Items each character has - top 20 =', curs5.execute(query5).fetchall())

curs6 = conn.cursor()
print('Weapons each character has - top 20 =', curs6.execute(query6).fetchall())

curs7 = conn.cursor()
print('Average items each character has =', curs7.execute(query7).fetchall())

curs8 = conn.cursor()
print('Average weapons each character has =', curs8.execute(query8).fetchall())

# Close cursors and commit
curs1.close()
curs2a.close()
curs2b.close()
curs2c.close()
curs2d.close()
curs2e.close()
curs3.close()
curs4a.close()
curs4b.close()
curs5.close()
curs6.close()
curs7.close()
curs8.close()
conn.commit()
