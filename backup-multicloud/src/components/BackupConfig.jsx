import React, { useState } from 'react'
import { motion } from 'framer-motion'
import { Database, Folder, Plus, Play } from 'lucide-react'

const BackupConfig = () => {
  const [sources, setSources] = useState([
    { id: 1, type: 'database', name: 'MySQL Production', path: 'localhost:3306/production', enabled: true },
    { id: 2, type: 'folder', name: 'Documents', path: '/home/user/documents', enabled: true },
    { id: 3, type: 'database', name: 'PostgreSQL', path: 'localhost:5432/app_db', enabled: false },
  ])

  const toggleSource = (id) => {
    setSources(sources.map(source => 
      source.id === id ? { ...source, enabled: !source.enabled } : source
    ))
  }

  return (
    <div className="space-y-6">
      {/* Quick Actions */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
        <motion.button
          whileHover={{ scale: 1.02 }}
          whileTap={{ scale: 0.98 }}
          className="glass-card p-6 text-left hover:bg-white/10 transition-all duration-300"
        >
          <div className="flex items-center space-x-4">
            <div className="w-12 h-12 bg-gradient-to-r from-green-500 to-emerald-500 rounded-xl flex items-center justify-center">
              <Play className="w-6 h-6 text-white" />
            </div>
            <div>
              <h3 className="font-semibold text-lg">Backup Agora</h3>
              <p className="text-sm text-gray-400">Executar backup imediato</p>
            </div>
          </div>
        </motion.button>

        <motion.button
          whileHover={{ scale: 1.02 }}
          whileTap={{ scale: 0.98 }}
          className="glass-card p-6 text-left hover:bg-white/10 transition-all duration-300"
        >
          <div className="flex items-center space-x-4">
            <div className="w-12 h-12 bg-gradient-to-r from-neon-cyan to-neon-purple rounded-xl flex items-center justify-center">
              <Plus className="w-6 h-6 text-black" />
            </div>
            <div>
              <h3 className="font-semibold text-lg">Nova Fonte</h3>
              <p className="text-sm text-gray-400">Adicionar banco ou pasta</p>
            </div>
          </div>
        </motion.button>
      </div>

      {/* Backup Sources */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="glass-card p-6"
      >
        <h3 className="text-xl font-semibold mb-4 flex items-center">
          <Database className="w-5 h-5 mr-2 text-neon-cyan" />
          Fontes de Backup
        </h3>
        
        <div className="space-y-3">
          {sources.map((source, index) => (
            <motion.div
              key={source.id}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.1 }}
              className="flex items-center justify-between p-4 bg-white/5 rounded-lg hover:bg-white/10 transition-all duration-300"
            >
              <div className="flex items-center space-x-4">
                <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${
                  source.type === 'database' 
                    ? 'bg-blue-500/20 text-blue-400' 
                    : 'bg-yellow-500/20 text-yellow-400'
                }`}>
                  {source.type === 'database' ? <Database className="w-5 h-5" /> : <Folder className="w-5 h-5" />}
                </div>
                <div>
                  <h4 className="font-medium">{source.name}</h4>
                  <p className="text-sm text-gray-400">{source.path}</p>
                </div>
              </div>
              
              <div className="flex items-center space-x-3">
                <span className={`text-sm px-2 py-1 rounded-full ${
                  source.enabled 
                    ? 'bg-green-500/20 text-green-400' 
                    : 'bg-gray-500/20 text-gray-400'
                }`}>
                  {source.enabled ? 'Ativo' : 'Inativo'}
                </span>
                <button
                  onClick={() => toggleSource(source.id)}
                  className={`w-12 h-6 rounded-full transition-all duration-300 ${
                    source.enabled ? 'bg-neon-cyan' : 'bg-gray-600'
                  }`}
                >
                  <div className={`w-5 h-5 bg-white rounded-full transition-all duration-300 ${
                    source.enabled ? 'translate-x-6' : 'translate-x-0.5'
                  }`}></div>
                </button>
              </div>
            </motion.div>
          ))}
        </div>
      </motion.div>

      {/* Backup Schedule */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3 }}
        className="glass-card p-6"
      >
        <h3 className="text-xl font-semibold mb-4">Agendamento</h3>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium mb-2">Frequência</label>
            <select className="w-full bg-white/10 border border-white/20 rounded-lg px-3 py-2 text-white">
              <option value="daily">Diário</option>
              <option value="weekly">Semanal</option>
              <option value="monthly">Mensal</option>
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium mb-2">Horário</label>
            <input 
              type="time" 
              defaultValue="22:00"
              className="w-full bg-white/10 border border-white/20 rounded-lg px-3 py-2 text-white"
            />
          </div>
        </div>
      </motion.div>
    </div>
  )
}

export default BackupConfig