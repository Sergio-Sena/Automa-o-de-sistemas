import React, { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { Terminal, CheckCircle, AlertCircle, Clock, Filter } from 'lucide-react'

const Logs = () => {
  const [logs, setLogs] = useState([
    { id: 1, timestamp: '2025-01-05 20:15:32', level: 'success', message: 'Backup MySQL concluído com sucesso', details: 'Arquivo: mysql_backup_20250105.sql.gz (2.1 GB)' },
    { id: 2, timestamp: '2025-01-05 20:15:28', level: 'info', message: 'Upload para Google Cloud Storage iniciado', details: 'Bucket: backup-multicloud-gcp' },
    { id: 3, timestamp: '2025-01-05 20:15:25', level: 'info', message: 'Upload para AWS S3 iniciado', details: 'Bucket: backup-multicloud-aws' },
    { id: 4, timestamp: '2025-01-05 20:15:20', level: 'info', message: 'Compressão do backup concluída', details: 'Taxa de compressão: 68%' },
    { id: 5, timestamp: '2025-01-05 20:14:45', level: 'info', message: 'Iniciando backup do banco MySQL', details: 'Host: localhost:3306' },
    { id: 6, timestamp: '2025-01-04 22:00:15', level: 'success', message: 'Backup agendado executado com sucesso', details: 'Todas as fontes processadas' },
    { id: 7, timestamp: '2025-01-04 22:00:10', level: 'warning', message: 'Pasta /tmp/cache não encontrada', details: 'Continuando sem backup desta pasta' },
  ])

  const [filter, setFilter] = useState('all')

  const filteredLogs = logs.filter(log => {
    if (filter === 'all') return true
    return log.level === filter
  })

  const getLogIcon = (level) => {
    switch (level) {
      case 'success':
        return <CheckCircle className="w-4 h-4 text-green-500" />
      case 'warning':
        return <AlertCircle className="w-4 h-4 text-yellow-500" />
      case 'error':
        return <AlertCircle className="w-4 h-4 text-red-500" />
      default:
        return <Clock className="w-4 h-4 text-blue-500" />
    }
  }

  const getLogColor = (level) => {
    switch (level) {
      case 'success':
        return 'border-l-green-500 bg-green-500/5'
      case 'warning':
        return 'border-l-yellow-500 bg-yellow-500/5'
      case 'error':
        return 'border-l-red-500 bg-red-500/5'
      default:
        return 'border-l-blue-500 bg-blue-500/5'
    }
  }

  return (
    <div className="space-y-6">
      {/* Log Stats */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          className="glass-card p-4 text-center"
        >
          <CheckCircle className="w-6 h-6 text-green-500 mx-auto mb-2" />
          <p className="text-lg font-bold text-green-400">156</p>
          <p className="text-xs text-gray-400">Sucessos</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.1 }}
          className="glass-card p-4 text-center"
        >
          <AlertCircle className="w-6 h-6 text-yellow-500 mx-auto mb-2" />
          <p className="text-lg font-bold text-yellow-400">3</p>
          <p className="text-xs text-gray-400">Avisos</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="glass-card p-4 text-center"
        >
          <AlertCircle className="w-6 h-6 text-red-500 mx-auto mb-2" />
          <p className="text-lg font-bold text-red-400">0</p>
          <p className="text-xs text-gray-400">Erros</p>
        </motion.div>

        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.3 }}
          className="glass-card p-4 text-center"
        >
          <Terminal className="w-6 h-6 text-neon-cyan mx-auto mb-2" />
          <p className="text-lg font-bold text-neon-cyan">159</p>
          <p className="text-xs text-gray-400">Total</p>
        </motion.div>
      </div>

      {/* Filters */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4 }}
        className="glass-card p-4"
      >
        <div className="flex items-center space-x-4">
          <Filter className="w-5 h-5 text-neon-cyan" />
          <div className="flex space-x-2">
            {['all', 'success', 'warning', 'error', 'info'].map((level) => (
              <button
                key={level}
                onClick={() => setFilter(level)}
                className={`px-3 py-1 rounded-full text-sm transition-all duration-300 ${
                  filter === level
                    ? 'bg-neon-cyan text-black'
                    : 'bg-white/10 text-gray-400 hover:text-white'
                }`}
              >
                {level === 'all' ? 'Todos' : level.charAt(0).toUpperCase() + level.slice(1)}
              </button>
            ))}
          </div>
        </div>
      </motion.div>

      {/* Logs List */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.5 }}
        className="glass-card p-6"
      >
        <h3 className="text-xl font-semibold mb-4 flex items-center">
          <Terminal className="w-5 h-5 mr-2 text-neon-cyan" />
          Logs do Sistema
        </h3>

        <div className="space-y-2 max-h-96 overflow-y-auto">
          {filteredLogs.map((log, index) => (
            <motion.div
              key={log.id}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: index * 0.05 }}
              className={`p-3 rounded-lg border-l-4 ${getLogColor(log.level)}`}
            >
              <div className="flex items-start space-x-3">
                {getLogIcon(log.level)}
                <div className="flex-1 min-w-0">
                  <div className="flex items-center justify-between">
                    <p className="font-medium text-sm">{log.message}</p>
                    <span className="text-xs text-gray-400 whitespace-nowrap ml-2">
                      {log.timestamp}
                    </span>
                  </div>
                  {log.details && (
                    <p className="text-xs text-gray-400 mt-1">{log.details}</p>
                  )}
                </div>
              </div>
            </motion.div>
          ))}
        </div>
      </motion.div>
    </div>
  )
}

export default Logs