import React, { useState } from 'react'
import { motion } from 'framer-motion'
import { Cloud, Key, TestTube, CheckCircle, AlertCircle } from 'lucide-react'

const CloudSettings = () => {
  const [providers, setProviders] = useState([
    {
      name: 'AWS S3',
      status: 'connected',
      config: {
        accessKey: 'AKIA****EXHLQ',
        secretKey: '****',
        bucket: 'backup-multicloud-aws',
        region: 'us-east-1'
      }
    },
    {
      name: 'Google Cloud Storage',
      status: 'connected',
      config: {
        projectId: 'backup-multicloud-app',
        keyFile: 'service-account.json',
        bucket: 'backup-multicloud-gcp'
      }
    }
  ])

  const testConnection = (providerName) => {
    // Simular teste de conexão
    console.log(`Testando conexão com ${providerName}...`)
  }

  return (
    <div className="space-y-6">
      {/* Cloud Providers */}
      {providers.map((provider, index) => (
        <motion.div
          key={provider.name}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: index * 0.1 }}
          className="glass-card p-6"
        >
          <div className="flex items-center justify-between mb-6">
            <div className="flex items-center space-x-3">
              <Cloud className="w-6 h-6 text-neon-cyan" />
              <h3 className="text-xl font-semibold">{provider.name}</h3>
              <div className="flex items-center space-x-2">
                {provider.status === 'connected' ? (
                  <>
                    <CheckCircle className="w-4 h-4 text-green-500" />
                    <span className="text-sm text-green-400">Conectado</span>
                  </>
                ) : (
                  <>
                    <AlertCircle className="w-4 h-4 text-red-500" />
                    <span className="text-sm text-red-400">Desconectado</span>
                  </>
                )}
              </div>
            </div>
            <motion.button
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
              onClick={() => testConnection(provider.name)}
              className="flex items-center space-x-2 px-4 py-2 bg-neon-purple/20 text-neon-purple border border-neon-purple/30 rounded-lg hover:bg-neon-purple/30 transition-all duration-300"
            >
              <TestTube className="w-4 h-4" />
              <span>Testar</span>
            </motion.button>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {Object.entries(provider.config).map(([key, value]) => (
              <div key={key}>
                <label className="block text-sm font-medium mb-2 capitalize">
                  {key.replace(/([A-Z])/g, ' $1').trim()}
                </label>
                <div className="relative">
                  <input
                    type={key.includes('secret') || key.includes('key') ? 'password' : 'text'}
                    value={value}
                    className="w-full bg-white/10 border border-white/20 rounded-lg px-3 py-2 pr-10 text-white placeholder-gray-400"
                    placeholder={`Digite ${key}`}
                  />
                  {(key.includes('secret') || key.includes('key')) && (
                    <Key className="absolute right-3 top-2.5 w-4 h-4 text-gray-400" />
                  )}
                </div>
              </div>
            ))}
          </div>
        </motion.div>
      ))}

      {/* Security Settings */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.3 }}
        className="glass-card p-6"
      >
        <h3 className="text-xl font-semibold mb-4 flex items-center">
          <Key className="w-5 h-5 mr-2 text-neon-cyan" />
          Configurações de Segurança
        </h3>
        
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <div>
              <h4 className="font-medium">Criptografia de Backups</h4>
              <p className="text-sm text-gray-400">Criptografar todos os backups com AES-256</p>
            </div>
            <button className="w-12 h-6 bg-neon-cyan rounded-full">
              <div className="w-5 h-5 bg-white rounded-full translate-x-6 transition-all duration-300"></div>
            </button>
          </div>

          <div className="flex items-center justify-between">
            <div>
              <h4 className="font-medium">Verificação de Integridade</h4>
              <p className="text-sm text-gray-400">Verificar checksums após upload</p>
            </div>
            <button className="w-12 h-6 bg-neon-cyan rounded-full">
              <div className="w-5 h-5 bg-white rounded-full translate-x-6 transition-all duration-300"></div>
            </button>
          </div>

          <div>
            <label className="block text-sm font-medium mb-2">Senha de Criptografia</label>
            <input
              type="password"
              className="w-full bg-white/10 border border-white/20 rounded-lg px-3 py-2 text-white placeholder-gray-400"
              placeholder="Digite uma senha forte"
            />
          </div>
        </div>
      </motion.div>

      {/* Save Button */}
      <motion.button
        whileHover={{ scale: 1.02 }}
        whileTap={{ scale: 0.98 }}
        className="w-full neon-button"
      >
        Salvar Configurações
      </motion.button>
    </div>
  )
}

export default CloudSettings